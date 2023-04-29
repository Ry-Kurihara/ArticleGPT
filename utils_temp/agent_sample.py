from langchain.llms import OpenAI

# Agent, Tools
from langchain.agents import AgentType, Tool, initialize_agent, tool
from langchain.tools import BaseTool
import asyncio 

# MyLibrary
from crowler.get_article_info import get_article_info
from article_creater.myprompts import prompt_make_article
# MyLibrary_Type
from typing import List
from crowler.get_article_info import Article

class CustomSearchTool(BaseTool):
    name = "SearchAndCreatePrompt"
    description = "useful to search target word on Google and create a prompt that enable LLM to produce an article"

    def _run(self, query: str) -> str:
        """Use the tool."""
        print(f"queryは{query}で受け取りました")
        search_word = "chatGPT"
        articles = asyncio.run(get_article_info(search_word))
        prompt = integrate_article(articles, search_word)
        return prompt
    
    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("BingSearchRun does not support async")
    
def integrate_article(articles: List[Article], search_word) -> str:
    integrated_contents = ""
    for i, article in enumerate(articles):
        integrated_contents += f"rank{i+1}title {article.title}\n"
        integrated_contents += f"{article.html_content}\n\n"

    prompt = prompt_make_article.format(search_word=search_word, integrated_contents=integrated_contents)
    return prompt

def run_agent_to_make_article():
    llm = OpenAI(model_name="gpt-4", temperature=0.7)
    tools = [CustomSearchTool(),]
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    agent.run("chatGPTという言葉について、Webで検索し、記事を作成するためのプロンプトを生成してください")

if __name__ == '__main__':
    run_agent_to_make_article()