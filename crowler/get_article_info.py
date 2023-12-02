import asyncio, os, requests
from dataclasses import dataclass

# playwright&html_parser
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

# Type definition
from typing import List
from playwright.sync_api import Browser, BrowserContext, Page, Locator
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


async def _get_page_title_and_content(browser: Browser, page_links: Iterable, search_word: str, max_words: int) -> List[SearchArticle]:
    tasks = []
    context = await browser.new_context()
    context.set_default_timeout(120000) # 120,000ms: 120s
    for url in page_links:
        page = await context.new_page()
        tasks.append(_fetch_page_content(page, url, search_word, max_words))
    articles = await asyncio.gather(*tasks)
    return articles

async def get_article_info(search_word: str, max_rank: int = 3, max_words: int = 2000) -> List[SearchArticle]:
    """
    max_words: 
    使用モデルの最大入力トークンを超過しないように指定する。
    モデルによって最大入力トークン（≒文字数）が変わる。gpt-4モデルで上限8192トークン。
    """
    urls = await _get_target_search_link_list(search_word, max_rank)

    async with async_playwright() as playwright:
        browser: Browser = await playwright.chromium.launch(headless=True)
        context: BrowserContext = await browser.new_context()
        context.set_default_timeout(60000) # 60,000ms: 60s

        articles = await _get_page_title_and_content(browser, urls, search_word, max_words)
        for article in articles:
            print(f"Title: {article.title}\nContent: {article.html_content[:300]}\n\n")

        return articles
    

if __name__ == '__main__':
    # for debug
    asyncio.run(_get_target_search_link_list("ワイヤレスイヤホン AZ80 比較", 3))