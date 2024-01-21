import asyncio, os, requests
from dataclasses import dataclass

# playwright&html_parser
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

# Type definition
from typing import List
from playwright.sync_api import Browser, BrowserContext, Page
from typing import Iterable

"""
Objects:
search_word → SearchArticle
"""

@dataclass
class SearchArticle:
    search_word: str
    title: str
    html_content: str


async def _get_target_search_link_list(search_word: str, max_rank: int) -> List[str]:
    """
    この関数内でGoogle Custom Search APIへのリクエストを行う
    参考: https://qiita.com/kingpanda/items/54043eddcf09699ceabc
    """
    api_key = os.environ["CSE_API_KEY"]
    cse_id = os.environ["CSE_ID"]
    query = search_word

    # 地域固有の検索結果を得るためのパラメータと検索言語、UI言語の指定
    params = {
        "key": api_key,
        "cx": cse_id,
        "q": query,
        "cr": "countryJP",  # 日本に特化した検索結果
        "lr": "lang_ja",    # 日本語の検索結果
        "hl": "ja"          # ユーザーインターフェースの言語を日本語に
    }

    print(f"start searching for: {search_word}")
    response = requests.get("https://www.googleapis.com/customsearch/v1", params=params)
    results = response.json()
    # max_rank: Google検索結果の上位何件を取得するか。10以下を指定すること。10位以降は2ページ目以降の検索結果になるが、そのページ処理は未実装。
    urls = [item["link"] for item in results.get("items", [])[:max_rank]]
    print(f"searched urls: {urls}")
    return urls


async def _fetch_page_content(page: Page, url: str, search_word: str, max_words: int) -> SearchArticle:
    await page.goto(url)
    # await page.pause()
    # user_agent = await page.evaluate("navigator.userAgent") # クロールするブラウザのVersionを確認するために使用
    # print(f"User Agent: {user_agent}")

    title: str = await page.title()
    content: str = await page.content()

    soup = BeautifulSoup(content, 'html.parser')
    for script in soup(['script', 'style']):
        script.extract()
    content = soup.get_text()
    content = " ".join(content.split())

    article = SearchArticle(search_word=search_word, title=title, html_content=content[:max_words])
    await page.close()
    return article


async def _get_page_title_and_content(context: BrowserContext, page_links: Iterable, search_word: str, max_words: int) -> List[SearchArticle]:
    tasks = []
    for url in page_links:
        page = await context.new_page()
        tasks.append(_fetch_page_content(page, url, search_word, max_words))
    articles = await asyncio.gather(*tasks)
    return articles

async def get_article_info(search_word: str, max_rank: int = 3, max_words: int = 2000) -> List[SearchArticle]:
    """
    max_words: 
    使用モデルの最大入力トークンを超過しないように指定する。

    最大入力トークン（≒文字数）：
        - gpt-4モデルで上限8192トークン。
        - gpt-4-turboで128,000トークン。gpt-4の16倍。

    料金（2024/01/07時点）：
        - GPT4-Turbo: Input:$0.01/1Ktokens Output:$0.03/1Ktokens
            - 1$=150円換算で、Input:1.5円/1Ktokens Output:4.5円/1Ktokens

    1実行あたりの試算（2024/01/07時点のGPT4-Turbo）：
        - 1記事あたりのトークン数を2000トークンとして、3記事分（max_rank=3）とすると、Inputが6000トークン。Outputは要約されて帰ってくるとして、3000トークンとする。
            - 実行コストは、Input:1.5*6=9円, Output:4.5*3=13.5円。合計22.5円。
            - 要約テキスト->記事テキスト出力コストはこれよりも少し安いと考えればOK。
    """
    urls = await _get_target_search_link_list(search_word, max_rank) # TODO: max_rankもコマンドライン引数で指定できるようにする。
    # urls = ['any_url'] # for debug

    async with async_playwright() as playwright:
        browser: Browser = await playwright.chromium.launch(headless=True) # Webサイトによってはheadlessモードだとアクセス拒否が発生することがある。その場合はheadless=Falseにする。
        device = playwright.devices["Desktop Chrome"] # 特定のデバイス環境を模倣できる。この引数を与えなくてもデフォルト設定でcontextを作成してくれるため特に問題は生じないが、一応設定しておく。
        context: BrowserContext = await browser.new_context(**device)
        context.set_default_timeout(60000) # 60,000ms: 60s

        articles = await _get_page_title_and_content(context, urls, search_word, max_words)
        for article in articles:
            print(f"Title: {article.title}\nContent: {article.html_content[:300]}\n\n")

        return articles
    

if __name__ == '__main__':
    # for debug
    # asyncio.run(_get_target_search_link_list("ワイヤレスイヤホン AZ80 比較", 3))
    asyncio.run(get_article_info("Twitter", 2))