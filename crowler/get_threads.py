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
class ThreadContents:
    thread_title: str
    html_content: str

async def _fetch_page_content(page: Page, url: str, max_words: int) -> ThreadContents:
    await page.goto(url)
    # await page.pause()
    title: str = await page.title()

    content: str = await page.content()
    soup = BeautifulSoup(content, 'html.parser')
    for script in soup(['script', 'style']):
        script.extract()
    content = soup.get_text()
    content = " ".join(content.split())

    thread = ThreadContents(thread_title=title, html_content=content[:max_words])
    await page.close()
    print(f"thread詳細: {thread.thread_title},\n {thread.html_content[:1000]}")
    print(f"threadの文字数: {len(thread.html_content)}")
    return thread

async def get_threads(urls: List[str], max_words: int) -> List[ThreadContents]:
    threads: List[ThreadContents] = []
    async with async_playwright() as playwright:
        browser: Browser = await playwright.chromium.launch(headless=True)
        context: BrowserContext = await browser.new_context()
        context.set_default_timeout(60000) # 60,000ms: 60s
        for url in urls:
            page: Page = await context.new_page()
            thread = await _fetch_page_content(page, url, max_words)
            threads.append(thread)
            await page.close()
        await context.close()
        await browser.close()
    return threads

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_threads(['https://kizuna.5ch.net/test/read.cgi/wm/1690439870/l50'], None))