import pytest
from unittest.mock import patch
from interpreter.summarize import _organize_integrated_contents, SummarizedSearchArticle

@pytest.fixture
def summarized_article():
    return SummarizedSearchArticle(search_word="今日の天気", title="Summary of 今日の天気", contents="<p>今日は晴れです。</p>")


# export PYTHONPATH=".:${PYTHONPATH}"等を実行してルートディレクトリをPYTHONPATHに追加しておいてください。
@patch("interpreter.summarize.ChatOpenAI")
@patch("interpreter.summarize.LLMChain")
def test_organize_html_contents(mocked_llm_chain, mocked_chat_openai, summarized_article):
    mocked_chat_openai.return_value = None
    _organize_integrated_contents(summarized_article)

    # ChatOpenAI, LLMChainのコンストラクタが期待通りに呼ばれたかどうかを確認
    mocked_chat_openai.assert_called_once()
    mocked_llm_chain.assert_called_once()
