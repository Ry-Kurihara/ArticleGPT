import asyncio 
from argparse import ArgumentParser, Namespace

from crowler.get_article_info import get_article_info
from interpreter.convert import convert_search_articles_into_blog_posting
from render.render_templates import render_summarized_search_article
from uploader.upload_file import upload_draft_to_wp


def get_args() -> Namespace:
    parser = ArgumentParser(description="Search for a specific word and crawl the high rank articles")
    parser.add_argument("search_word", nargs='+', help="The word to search for")
    parser.add_argument("--max_rank", type=int, default=3, help="The number of articles to get from the top of Google search")
    parser.add_argument("--max_page_chars", type=int, default=5000, help="Maximum number of characters per getted page.")
    parser.add_argument("--comment_num", type=int, default=25, help="Number of comments to generate.")
    parser.add_argument("--need_summary", type=str, default="no", help="Whether to summarize the articles.")
    args = parser.parse_args()
    args.search_word = ' '.join(args.search_word)  # Converts list of words into a single string
    return args


if __name__ == '__main__':
    args = get_args()
    # crowler
    search_articles = asyncio.run(get_article_info(args.search_word, max_rank=args.max_rank, max_words=args.max_page_chars))

    # interpreter
    need_summary = False if args.need_summary == "no" else True
    blog_posting = convert_search_articles_into_blog_posting(search_articles, comment_num=args.comment_num, need_summary=need_summary)

    # render
    render_summarized_search_article(blog_posting)

    # uploader
    html_file_name = f"render/output/2ch/{blog_posting.title}.html"
    upload_draft_to_wp(html_file_name)