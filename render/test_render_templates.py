import os
import pytest
from unittest.mock import patch, mock_open
from render.render_templates import Format2chSummarizedSearchArticle, render_summarized_search_article, render_specified_tpl_path
from interpreter.summarize import SummarizedSearchArticle


@pytest.fixture
def summarized_article():
    article = SummarizedSearchArticle(
        search_word="test_dayo",
        title="test_title",
        contents="{%- set sample = 'aiueo' %} This is {{ sample }}"
    )
    return article


def test_Format2chSummarizedSearchArticle_render(summarized_article):
    renderer = Format2chSummarizedSearchArticle(summarized_article)
    renderer.write_tpl_from_object()

    # tplファイルが作成されているか
    tpl_file_path = f"render/output/2ch/{summarized_article.title}.html.tpl"
    assert os.path.exists(tpl_file_path)

    # tplファイルがレンダリングされてhtmlファイルが生成されているか
    renderer.render()
    html_file_path = f"render/output/2ch/{summarized_article.title}.html"
    assert os.path.exists(html_file_path)

    os.remove(html_file_path)
    os.remove(tpl_file_path)


def test_render_specified_tpl_path(summarized_article):
    """
    mockのbuiltin.open環境にsummarized_articleから作成されるtplオブジェクトを作成する
    そのmock環境でrenderされて正常なhtmlファイルが作成されるか確認する
    """

