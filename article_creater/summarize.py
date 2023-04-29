from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain, SimpleSequentialChain

# Agent, Tools
import asyncio 

# MyLibrary
from crowler.get_article_info import get_article_info
from article_creater.myprompts import prompt_enable_llm_to_make_articles, prompt_summarize_each_article
# MyLibrary_Type
from typing import List
from crowler.get_article_info import Article

def integrate_article_html_contents(articles: List[Article]) -> str:
    integrated_contents = ""
    for i, article in enumerate(articles):
        integrated_contents += f"rank{i+1}title {article.title}\n"
        integrated_contents += f"{article.html_content}\n\n"

    return integrated_contents

def summarize_html_contents(articles: List[Article]) -> List[Article]:
    llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)
    chain = LLMChain(llm=llm, prompt=prompt_summarize_each_article)
    summerized_articles = []
    # HACK: 並列処理にして実行時間を短縮したい
    for article in articles:
        summary = chain.run({"title": article.title, "html_contents": article.html_content})
        print(f"{article.title}の要約結果: {summary}")
        summerized_articles.append(Article(title=article.title, html_content=summary))
    return summerized_articles

def create_chain():
    llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)
    chain_make_articles = LLMChain(llm=llm, prompt=prompt_enable_llm_to_make_articles)
    

if __name__ == '__main__':
    articles = asyncio.run(get_article_info("LangChain"))
    summarize_html_contents(articles)