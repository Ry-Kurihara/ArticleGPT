import asyncio 
from argparse import ArgumentParser, Namespace

from crowler.get_article_info import get_article_info
from interpreter.summarize import summarize_search_articles
from render.render_templates import render_summarized_search_article, render_specified_tpl_path

def get_args() -> Namespace:
    parser = ArgumentParser(description="Search for a specific word and crawl the high rank articles")
    parser.add_argument("search_word", help="The word to search for")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = get_args()
    search_articles = asyncio.run(get_article_info(args.search_word))
    sumarized = asyncio.run(summarize_search_articles(search_articles))
    render_summarized_search_article(sumarized)
    # render_specified_tpl_path(f"Summary_of_{search_word}")
    
    