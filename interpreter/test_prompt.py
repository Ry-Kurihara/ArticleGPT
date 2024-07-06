import pytest 
from interpreter.prompt import summarize_pmt, MakeConversationPrompt, MakeTitlePrompt

def test_summerize_pmt_if_arg_num_is_same_with_hard_cord():
    actual_chat_pmt = summarize_pmt()
    assert set(actual_chat_pmt.input_variables) == set(['title', 'word_count', 'html_contents']) # プログラム中に入力されるプロンプトを想定してハードコードしている

def test_make_conversation_pmt_if_arg_num_is_correct():
    # actual_args（プログラム中にプロンプトに実際に入力される変数）の数が、expected_args(sys_pmtのvariables + human_pmtのvariables: プロンプトが期待している変数の数)と一致するか
    prompt_class = MakeConversationPrompt()
    actual_args = set(prompt_class.variables("test_word", "test_summary").keys()) # 必須項目だけ引数として与えるが、デフォルト引数も辞書にセットされて帰ってくるので、実質は引数全ての数が返ってくる。
    expected_args = set(prompt_class.pmt_tmpl().input_variables) 
    assert actual_args == expected_args

def test_make_title_pmt_if_arg_num_is_correct():
    prompt_class = MakeTitlePrompt()
    actual_args = set(prompt_class.variables("test_article_contents").keys())
    expected_args = set(prompt_class.pmt_tmpl().input_variables)
    assert actual_args == expected_args