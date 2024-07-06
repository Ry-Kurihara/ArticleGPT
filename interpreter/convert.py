from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
from langchain.callbacks.tracers import ConsoleCallbackHandler

# Tools
import os
from dataclasses import dataclass

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
    contents: str # tpl形式の文字列。後続の処理でHTMLに変換するためのもの。

@dataclass
class IntegratedSearchArticle:
    search_word: str
    contents: str

def _print_articles(articles: List[SearchArticle]) -> None:
    for article in articles:
        print(f"Search_Word: {article.search_word} \nTitle: {article.title} \nPrint_Contents: {article.html_content} \n")


def _summarize_each_html_contents(llm: ChatOpenAI|ChatAnthropic, articles: List[SearchArticle], summary_word_count: int) -> List[SearchArticle]:
    prompt = summarize_pmt()
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    input_dicts = [{"title": article.title, "html_contents": article.html_content, "word_count": summary_word_count} for article in articles]
    summarized_html_contents: List[str] = chain.batch(input_dicts)
    summarized_search_articles = [SearchArticle(article.search_word, article.title, summarized_html_contents[i]) for i, article in enumerate(articles)]
    return summarized_search_articles


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


def _convert_integrated_search_article_into_blog_posting(llm: ChatOpenAI|ChatAnthropic, integrated_search_article: IntegratedSearchArticle, comment_num: int) -> BlogPosting:
    prompt_class = MakeConversationPrompt()
    prompt = prompt_class.pmt_tmpl()
    chain_input = prompt_class.variables(integrated_search_article.search_word, integrated_search_article.contents, "nan_j", comment_num)
    
    chain = prompt | llm | StrOutputParser()
    console = {'callbacks': [ConsoleCallbackHandler()]} # HACK: set_verbose(True)が効かないためこちらで代用中
    resp_contents = chain.invoke(chain_input, config=console)
    resp_title = _make_title_from_contents(llm, resp_contents)
    return BlogPosting(integrated_search_article.search_word, resp_title, resp_contents)


def _make_title_from_contents(llm: ChatOpenAI|ChatAnthropic, contents: str) -> str:
    prompt_class = MakeTitlePrompt()
    prompt = prompt_class.pmt_tmpl()
    chain_input = prompt_class.variables(article_contents=contents)

    chain = prompt | llm | StrOutputParser()
    llm_resp = chain.invoke(chain_input)
    return llm_resp


def _create_llm_model() -> ChatOpenAI | ChatAnthropic:
    use_model = os.environ["LLM_MODEL_NAME"]
    if use_model == "GPT":
        # 環境変数OPENAI_API_KEYを参照します。
        llm = ChatOpenAI(model_name="gpt-4o", temperature=0.7, request_timeout=180)
    elif use_model == "CLAUDE":
        # 環境変数ANTHROPIC_API_KEYを参照します。
        llm = ChatAnthropic(model_name="claude-3-haiku-20240307")
    return llm


def convert_search_articles_into_blog_posting(articles: List[SearchArticle], summary_word_count: int = 1000, comment_num: int = 25, need_summary: bool = False) -> BlogPosting:
    """
    summary_word_count: 記事要約の文字数。この文字数*要約記事数（だいたい3くらい）がLLMに入力される。
    """
    llm = _create_llm_model()
    each_articles = _summarize_each_html_contents(llm, articles, summary_word_count) if need_summary else articles
    _print_articles(each_articles)
    integrated = _integrate_search_articles(each_articles)
    blog_posting = _convert_integrated_search_article_into_blog_posting(llm, integrated, comment_num)
    return blog_posting


if __name__ == '__main__':
    # デバッグ用：python -m interpreter.convert
    # set_debug(True) # set_verbose(True) or set_debug(True)
    sa = SearchArticle(search_word="今日の天気", title="気象庁 天気予報", html_content="<p>今日は晴れです。</p>")
    # _summarize_each_html_contents([sa, sa], 1000)
    convert_search_articles_into_blog_posting([sa, sa], 1000, 25, False)