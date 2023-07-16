from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

# Tools
import asyncio 
from dataclasses import dataclass
# Tools Type
from asyncio import Task

# MyLibrary
from interpreter.prompt import summarize_pmt, ConversationPrompt
# MyLibrary_Type
from typing import List
from crowler.get_article_info import SearchArticle

"""
Objects:
SearchArticle | List[SearchArticle] → SummarizedSearchArticle
"""

@dataclass
class SummarizedSearchArticle:
    search_word: str
    title: str
    contents: str


def _print_articles(articles: List[SearchArticle]) -> None:
    for article in articles:
        print(f"Search_Word: {article.search_word} \nTitle: {article.title} \nPrint_Article: {article.html_content} \n")


async def _summarize_each_html_contents(articles: List[SearchArticle], summary_word_count: int) -> List[SearchArticle]:
    llm = ChatOpenAI(model_name="gpt-4", temperature=0.5)
    chain = LLMChain(llm=llm, prompt=summarize_pmt(), verbose=True)

    async def run_chain(article: SearchArticle) -> Task[SearchArticle]:
        summary = await chain.arun({"title": article.title, "html_contents": article.html_content, "word_count": summary_word_count})
        return SearchArticle(article.search_word, article.title, summary)  

    tasks = [run_chain(article) for article in articles]
    return await asyncio.gather(*tasks)


def _integrate_search_articles(articles: List[SearchArticle]) -> SummarizedSearchArticle:
    integrated_contents = ""
    search_word = articles[0].search_word # 全て同じsearch_wordのためどこからとっても良い
    for i, article in enumerate(articles):
        integrated_contents += f"rank{i+1}_title {article.title}:\n"
        integrated_contents += f"{article.html_content}\n\n"
    summarized_article = SummarizedSearchArticle(
        search_word=search_word,
        title=f"Summary_of_{search_word}",
        contents=integrated_contents
    )
    return summarized_article


def _organize_integrated_contents(summarized_article: SummarizedSearchArticle) -> SummarizedSearchArticle:
    llm = ChatOpenAI(model_name="gpt-4", temperature=0.7, request_timeout=180)
    prompt_class = ConversationPrompt()
    prompt = prompt_class.pmt_tmpl()
    chain_input = prompt_class.variables(summarized_article.search_word, summarized_article.contents, "nan_j", 20) # HACK: commentの数はmainモジュールのargsparseクラスから取ってくる
    chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
    llm_resp = chain.run(chain_input)
    # TODO: memoryでこのタイトルを考えてくださいを実現する
    return SummarizedSearchArticle(summarized_article.search_word, summarized_article.title, llm_resp)


async def summarize_search_articles(articles: List[SearchArticle], summary_word_count: int = 700) -> SummarizedSearchArticle:
    """
    summary_word_count: 記事要約の文字数。この文字数*要約記事数（だいたい3くらい）がLLMに入力される。
    """
    summarized_each_articles = await _summarize_each_html_contents(articles, summary_word_count)
    _print_articles(summarized_each_articles)
    integrated = _integrate_search_articles(summarized_each_articles)
    organized = _organize_integrated_contents(integrated)
    return organized