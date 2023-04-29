from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain, SimpleSequentialChain

# Tools
import asyncio 
# Tools Type
from asyncio import Task

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


async def summarize_html_contents_async(articles: List[Article]) -> List[Article]:
    llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)
    chain = LLMChain(llm=llm, prompt=prompt_summarize_each_article)

    async def run_chain(article: Article) -> Task[Article]:
        summary = await chain.arun({"title": article.title, "html_contents": article.html_content})
        return Article(article.title, summary)  

    tasks = [run_chain(article) for article in articles]
    return await asyncio.gather(*tasks)


def print_articles(articles: List[Article]) -> None:
    for article in articles:
        print(f"Title: {article.title} \nPrint_Article: {article.html_content} \n")
   

if __name__ == '__main__':
    articles = asyncio.run(get_article_info("LangChain"))
    summarized_articles = asyncio.run(summarize_html_contents_async(articles))
    print_articles(summarized_articles)