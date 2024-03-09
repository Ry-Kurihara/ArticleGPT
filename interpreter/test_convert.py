import pytest
from unittest.mock import patch
from interpreter.convert import convert_search_articles_into_blog_posting, SearchArticle

@pytest.fixture
def dummy_search_articles():
    sa = SearchArticle(search_word="今日の天気", title="気象庁 天気予報", html_content="<p>今日は晴れです。</p>")
    return [sa, sa]

@patch("interpreter.convert._convert_integrated_search_article_into_blog_posting")
@patch("interpreter.convert._summarize_each_html_contents")
def test_convert_with_need_summary(m_summ, m_conv, dummy_search_articles):
    convert_search_articles_into_blog_posting(dummy_search_articles, need_summary=True)
    m_summ.assert_called_once()
    m_conv.assert_called_once()

@patch("interpreter.convert._convert_integrated_search_article_into_blog_posting")
@patch("interpreter.convert._summarize_each_html_contents")
def test_convert_without_need_summary(m_summ, m_conv, dummy_search_articles):
    convert_search_articles_into_blog_posting(dummy_search_articles, need_summary=False)
    m_summ.assert_not_called()
    m_conv.assert_called_once()
