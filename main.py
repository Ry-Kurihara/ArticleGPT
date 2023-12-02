import asyncio 
from argparse import ArgumentParser, Namespace

from crowler.get_article_info import get_article_info
from interpreter.summarize import summarize_search_articles
from render.render_templates import render_summarized_search_article
from uploader.upload_file import upload_draft_to_wp


def get_args() -> Namespace:
    parser = ArgumentParser(description="Search for a specific word and crawl the high rank articles")
    parser.add_argument("search_word", nargs='+', help="The word to search for")
    args = parser.parse_args()
    args.search_word = ' '.join(args.search_word)  # Converts list of words into a single string
    return args


if __name__ == '__main__':
    args = get_args()
    # crowler
    search_articles = asyncio.run(get_article_info(args.search_word))

    # interpreter
    sumarized = asyncio.run(summarize_search_articles(search_articles))

    # render
    render_summarized_search_article(sumarized)

    # uploader
    html_file_name = f"render/output/2ch/{sumarized.title}.html"
    upload_draft_to_wp(html_file_name)