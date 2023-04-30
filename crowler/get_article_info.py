import asyncio
from dataclasses import dataclass

# playwright&html_parser
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

# Type definition
from typing import List
from playwright.sync_api import Browser, BrowserContext, Page, Locator
from typing import Iterable

@dataclass
class Article:
    title: str
    html_content: str

async def _get_target_search_link_list(page: Page, search_word: str, max_rank: int) -> List[str]:
    await page.goto("https://www.google.com")

    print(f"starting search for: {search_word}")
    search_input: Locator = page.locator('.gLFyf')
    await search_input.type(search_word)
    await search_input.press("Enter")

    await page.wait_for_load_state("load")
    await page.screenshot(path="temp_debug/images/ss_search_result.png")

    search_results = page.locator(".tF2Cxc")
    search_results_links = search_results.locator(".yuRUbf > a")

    urls = []
    for i in range(max_rank):
        try:
            link = search_results_links.nth(i)
            url = await link.get_attribute("href")
            urls.append(url)
        except Exception as e:
            print(f"Error getting the link at index {i}: {e}")

    await page.close()
    return urls


async def _fetch_page_content(page: Page, url: str, max_words: int) -> Article:
    await page.goto(url)
    # await page.pause()
    title: str = await page.title()

    content: str = await page.content()
    soup = BeautifulSoup(content, 'html.parser')
    for script in soup(['script', 'style']):
        script.extract()
    content = soup.get_text()
    content = " ".join(content.split())

    article = Article(title=title, html_content=content[:max_words])
    await page.close()
    return article


async def _get_page_title_and_content(browser: Browser, page_links: Iterable, max_words: int) -> List[Article]:
    tasks = []
    context = await browser.new_context()
    for url in page_links:
        page = await context.new_page()
        tasks.append(_fetch_page_content(page, url, max_words))
    articles = await asyncio.gather(*tasks)
    return articles

async def get_article_info(search_word: str, max_rank: int = 3, max_words: int = 5000) -> List[Article]:
    """
    max_words: 
    使用モデルの最大入力トークンを超過しないように指定する。
    モデルによって最大入力トークン（≒文字数）が変わる。gpt-4モデルで上限8192トークン。
    """
    async with async_playwright() as playwright:
        browser: Browser = await playwright.chromium.launch(headless=True)
        context: BrowserContext = await browser.new_context()
        context.set_default_timeout(30000) # 30,000ms: 30s
        page: Page = await context.new_page()

        urls = await _get_target_search_link_list(page, search_word, max_rank)
        print(f"urls: {urls}")

        articles = await _get_page_title_and_content(browser, urls, max_words)
        for article in articles:
            print(f"Title: {article.title}\nContent: {article.html_content[:300]}\n\n")

        return articles
