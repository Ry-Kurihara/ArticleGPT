from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

# Tools
import asyncio 
from dataclasses import dataclass
# Tools Type
from asyncio import Task

# MyLibrary
from interpreter.prompt import summarize_pmt, MakeConversationPrompt, MakeTitlePrompt
# MyLibrary_Type
from typing import List
from crowler.get_article_info import SearchArticle

"""
Objects:
SearchArticle | List[SearchArticle] → BlogPosting
"""

@dataclass
class BlogPosting:
    search_word: str
    title: str
    contents: str # tpl形式の文字列。これをjinja2でレンダリングしてhtmlにする。

@dataclass
class IntegratedSearchArticle:
    search_word: str
    contents: str

def _print_articles(articles: List[SearchArticle]) -> None:
    for article in articles:
        print(f"Search_Word: {article.search_word} \nTitle: {article.title} \nPrint_Article: {article.html_content} \n")


async def _summarize_each_html_contents(articles: List[SearchArticle], summary_word_count: int) -> List[SearchArticle]:
    llm = ChatOpenAI(model_name="gpt-3.5-turbo-16k", temperature=0.5)
    chain = LLMChain(llm=llm, prompt=summarize_pmt(), verbose=True)

    async def run_chain(article: SearchArticle) -> Task[SearchArticle]:
        summary = await chain.arun({"title": article.title, "html_contents": article.html_content, "word_count": summary_word_count})
        return SearchArticle(article.search_word, article.title, summary)  

    tasks = [run_chain(article) for article in articles]
    return await asyncio.gather(*tasks)


def _integrate_search_articles(articles: List[SearchArticle]) -> IntegratedSearchArticle:
    integrated_contents = ""
    search_word = articles[0].search_word # 全て同じsearch_wordのためどこからとっても良い
    for i, article in enumerate(articles):
        integrated_contents += f"rank{i+1}_title {article.title}:\n"
        integrated_contents += f"{article.html_content}\n\n"
    summarized_article = IntegratedSearchArticle(
        search_word=search_word,
        contents=integrated_contents
    )
    return summarized_article


def _convert_integrated_search_article_into_blog_posting(integrated_search_article: IntegratedSearchArticle, comment_num: int) -> BlogPosting:
    llm = ChatOpenAI(model_name="gpt-4-1106-preview", temperature=0.7, request_timeout=180)
    prompt_class = MakeConversationPrompt()
    prompt = prompt_class.pmt_tmpl()
    chain_input = prompt_class.variables(integrated_search_article.search_word, integrated_search_article.contents, "ordinary", comment_num)
    chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
    llm_resp = chain.run(chain_input)
    llm_title = _make_title_from_contents(llm_resp)
    return BlogPosting(integrated_search_article.search_word, llm_title, llm_resp)


def _make_title_from_contents(contents: str) -> str:
    llm = ChatOpenAI(model_name="gpt-4-1106-preview", temperature=0.7, request_timeout=180)
    prompt_class = MakeTitlePrompt()
    prompt = prompt_class.pmt_tmpl()
    chain_input = prompt_class.variables(article_contents=contents)
    chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
    llm_resp = chain.run(chain_input)
    return llm_resp


async def convert_search_articles_into_blog_posting(articles: List[SearchArticle], summary_word_count: int = 1000, comment_num: int = 25, need_summary: bool = False) -> BlogPosting:
    """
    summary_word_count: 記事要約の文字数。この文字数*要約記事数（だいたい3くらい）がLLMに入力される。
    """
    each_articles = await _summarize_each_html_contents(articles, summary_word_count) if need_summary else articles
    _print_articles(each_articles)
    integrated = _integrate_search_articles(each_articles)
    blog_posting = _convert_integrated_search_article_into_blog_posting(integrated, comment_num)
    return blog_posting