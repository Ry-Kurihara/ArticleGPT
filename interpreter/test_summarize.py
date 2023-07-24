import pytest
from unittest.mock import patch
from interpreter.summarize import _organize_integrated_contents, _make_title_from_contents, IntegratedSearchArticle

@pytest.fixture
def integrated_article():
    return IntegratedSearchArticle(search_word="今日の天気", contents="<p>今日は晴れです。</p>")


# export PYTHONPATH=".:${PYTHONPATH}"等を実行してルートディレクトリをPYTHONPATHに追加しておいてください。
@patch("interpreter.summarize.ChatOpenAI")
@patch("interpreter.summarize.LLMChain")
@patch("interpreter.summarize._make_title_from_contents")
def test_organize_html_contents(mocked_make_title, mocked_llm_chain, mocked_chat_openai, integrated_article):
    mocked_chat_openai.return_value = None
    mocked_make_title.return_value = "test_dayo"
    _organize_integrated_contents(integrated_article)

    # ChatOpenAI, LLMChainのコンストラクタが期待通りに呼ばれたかどうかを確認
    mocked_chat_openai.assert_called_once()
    mocked_llm_chain.assert_called_once()


@patch("interpreter.summarize.ChatOpenAI")
@patch("interpreter.summarize.LLMChain")
def test_make_title_from_contents(mocked_llm_chain, mocked_chat_openai):
    mocked_chat_openai.return_value = None
    _make_title_from_contents("aiueo")

    # ChatOpenAI, LLMChainのコンストラクタが期待通りに呼ばれたかどうかを確認
    mocked_chat_openai.assert_called_once()
    mocked_llm_chain.assert_called_once()
