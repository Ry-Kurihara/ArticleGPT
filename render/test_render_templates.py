import os
import pytest
from render.render_templates import SecondChFormatter, QiitaFormatter
from interpreter.summarize import SummarizedSearchArticle


@pytest.fixture
def summarized_article():
    article = SummarizedSearchArticle(
        search_word="test_dayo",
        title="test_title",
        contents="{%- set sample = 'aiueo' %} This is {{ sample }}"
    )
    return article


def test_2ch_formatter(summarized_article):
    output_dir = "2ch"
    renderer = SecondChFormatter(output_dir)
    file_name = summarized_article.title
    renderer.write_tpl_from_object(summarized_article, file_name)

    # tplファイルが作成されているか
    tpl_file_path = f"render/output/{output_dir}/{file_name}.html.tpl"
    assert os.path.exists(tpl_file_path)

    # tplファイルがレンダリングされてhtmlファイルが生成されているか
    renderer.render(file_name)
    html_file_path = f"render/output/{output_dir}/{file_name}.html"
    assert os.path.exists(html_file_path)

    os.remove(html_file_path)
    os.remove(tpl_file_path)


def test_qiita_formatter(summarized_article):
    output_dir = "qiita"
    renderer = QiitaFormatter(output_dir)
    file_name = summarized_article.title
    renderer.write_tpl_from_object(summarized_article, file_name)

    # tplファイルが作成されているか
    tpl_file_path = f"render/output/{output_dir}/{file_name}.html.tpl"
    assert os.path.exists(tpl_file_path)

    # tplファイルがレンダリングされてhtmlファイルが生成されているか
    renderer.render(file_name)
    html_file_path = f"render/output/{output_dir}/{file_name}.html"
    assert os.path.exists(html_file_path)

    os.remove(html_file_path)
    os.remove(tpl_file_path)


def test_qiita_with_specified_path():
    html_file_path = f"render/output/tests/for_test.html"
    os.remove(html_file_path)

    renderer = QiitaFormatter(output_dir="tests")
    renderer.render("for_test")
    assert os.path.exists(html_file_path)