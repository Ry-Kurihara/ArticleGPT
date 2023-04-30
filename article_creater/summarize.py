from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain, SimpleSequentialChain

# Tools
import asyncio 
# Tools Type
from asyncio import Task

# MyLibrary
from crowler.get_article_info import get_article_info
from article_creater.prompt_creater import create_template_enable_llm_to_make_articles, prompt_summarize_each_article
# MyLibrary_Type
from typing import List
from crowler.get_article_info import Article


def integrate_article_html_contents(articles: List[Article]) -> str:
    integrated_contents = ""
    for i, article in enumerate(articles):
        integrated_contents += f"rank{i+1}_title {article.title}:\n"
        integrated_contents += f"{article.html_content}\n\n"

    return integrated_contents


async def summarize_html_contents(articles: List[Article]) -> List[Article]:
    llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)
    chain = LLMChain(llm=llm, prompt=prompt_summarize_each_article)

    async def run_chain(article: Article) -> Task[Article]:
        summary = await chain.arun({"title": article.title, "html_contents": article.html_content})
        return Article(article.title, summary)  

    tasks = [run_chain(article) for article in articles]
    return await asyncio.gather(*tasks)


def create_article(search_word: str, integrated_summary: str) -> None:
    llm = ChatOpenAI(model_name="gpt-4", temperature=0.7, request_timeout=180)
    prompt = create_template_enable_llm_to_make_articles()
    chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
    resp = chain.run({"search_word": search_word, "integrated_summary": integrated_summary})
    
    with open("temp_debug/logs/sample.html", "w", encoding="utf-8") as f:
        f.write(resp)

def _print_articles(articles: List[Article]) -> None:
    for article in articles:
        print(f"Title: {article.title} \nPrint_Article: {article.html_content} \n")
   

if __name__ == '__main__':
    search_word = "SONY ZX707"
    articles = asyncio.run(get_article_info(search_word))
    summarized_articles = asyncio.run(summarize_html_contents(articles))
    _print_articles(summarized_articles)
    integrated_summary = integrate_article_html_contents(summarized_articles)
    print(f"Integrate:\n{integrated_summary}")

    resp = create_article(search_word, integrated_summary)
    print(f"final_resp: {resp}")