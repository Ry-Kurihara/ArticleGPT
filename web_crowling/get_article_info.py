import asyncio
from argparse import ArgumentParser
from dataclasses import dataclass

# playwright
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright

# Type definition
from typing import List
from playwright.sync_api import Browser, BrowserContext, Page, Locator

# Type define
from typing import Iterable

@dataclass
class Article:
    title: str
    html_content: str

def get_target_search_link_list(page: Page, search_word) -> List[str]:
    page.goto("https://www.google.com")

    print(f"starting search for: {search_word}")
    # print(f"page_content: {page.content()}")
    search_input: Locator = page.locator('.gLFyf')
    search_input.type(search_word)
    search_input.press("Enter")

    page.wait_for_load_state("load")
    page.screenshot(path="ss_search_result.png")

    search_results = page.locator(".tF2Cxc")
    search_results_links = search_results.locator(".yuRUbf > a")

    urls = []
    for i in range(5):
        try:
            link = search_results_links.nth(i)
            url = link.get_attribute("href")
            urls.append(url)
        except Exception as e:
            print(f"Error getting the link at index {i}: {e}")

    return urls

def get_page_title_and_content(page: Page, page_links: Iterable):
    """
    page_linkを複数受け取って、それらの記事のタイトルと記事本文500文字程度を抽出してArticleオブジェクトに格納する。
    page_linkは配列形式で最大10程度まで受け取ることを想定している。すべての記事に対して逐次処理をするのは無駄が多いため、それぞれの記事に対して並列処理を実行したい。
    """
    # 記述してください。
    pass

async def main():
    parser = ArgumentParser(description="Search for a specific word and crawl the top 5 articles")
    parser.add_argument("search_word", help="The word to search for")
    args = parser.parse_args()

    async with async_playwright() as playwright:
        browser: Browser = await playwright.chromium.launch(headless=False)
        context: List[BrowserContext] = await browser.new_context()
        page: Page = await context.new_page

        urls = await get_target_search_link_list(page, args.search_word)
        print(f"urls: {urls}")
        articles = await get_page_title_and_content(browser, urls)

        for article in articles:
            print(f"Title: {article.title}\nContent: {article.html_content}\n\n")

def main():
    parser = ArgumentParser(description="Search for a specific word and crawl the top 5 articles")
    parser.add_argument("search_word", help="The word to search for")
    args = parser.parse_args()

    with sync_playwright() as playwright:
        browser: Browser = playwright.chromium.launch(headless=False)
        context: List[BrowserContext] = browser.new_context()
        page: Page = context.new_page()

        urls = get_target_search_link_list(page, args.search_word)
        print(f"urls: {urls}")

if __name__ == "__main__":
    main()
