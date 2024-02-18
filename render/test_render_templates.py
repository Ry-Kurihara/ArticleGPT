import pytest
import os, textwrap
from render.render_templates import SecondChFormatter, QiitaFormatter
from interpreter.convert import BlogPosting


@pytest.fixture
def summarized_article():
    article = BlogPosting(
        search_word="test_dayo",
        title="python_test_title",
        contents=textwrap.dedent("""
            {%- set comments =[
                {'date': '2023/04/01 00:03:20.55', 'id': 'dCTjJxeka', 'res_index':'1', 'res':'今日は良い天気！', 'color':'blue', 'size':'20px'},
                {'date': '2023/04/01 00:55:20.33', 'id': 'acBTTT7k', 'res_index':'2', 'res':'>>2<br/>いや、そんなに良くないね', 'color':'red'},
                {'date': '2023/04/02 03:50:20.10', 'id': 'll88J7k', 'res_index':'3', 'res': '午後からは雨が降るらしいぞ'},
                {'date': '2023/04/04 11:10:20.04', 'id': 'kk77jLO3', 'res_index':'4', 'res': '>>3<br/>それどこ情報？？'},
                {'date': '2023/04/05 13:20:20.04', 'id': 'll88J7k', 'res_index':'5', 'res': '>>4<br/>いや、俺の勘www', 'size': '24px'},
            ] -%}
        """) # conversation.txtでは{{%- と -%}}で囲んでいるが、ここでは{%- と -%}で囲まないとエラーになる。理由としては、prompts.pyでload_prompt()の際に自動でf"{contents}"のように文字列に変換されるためかもしれない。f-stringを使用する際は波括弧を文字列として扱いたい場合は二重に囲む必要がある。
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


def test_with_specified_path():
    html_file_path = f"render/output/tests/for_test.html"
    if os.path.exists(html_file_path):
        os.remove(html_file_path)
    renderer = SecondChFormatter(output_dir="tests") # 任意のフォーマッタに変更してOK
    renderer.render("for_test")
    assert os.path.exists(html_file_path)