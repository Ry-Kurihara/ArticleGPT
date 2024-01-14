import pytest 
from interpreter.prompt import summarize_pmt, MakeConversationPrompt

def test_prompt():
    input_set = {"word_count": 200, "title": "test_title", "html_contents": "test_contents"}
    actual_chat_pmt = summarize_pmt()
    # assert actual_chat_pmt.format_messages(word_count=300, title="aiueo", html_contents="testes") == "aa"
    assert set(actual_chat_pmt.input_variables) == set(['title', 'word_count', 'html_contents'])

def test_prompt_enable_llm_to_convert_format_to_2ch():
    prompt_class = MakeConversationPrompt()
    actual_chat_pmt = prompt_class.pmt_tmpl()
    actual_input_variables = set(actual_chat_pmt.input_variables)
    expected_input_variables = set(['search_word', 'integrated_summary', 'personality', 'comments_count', 'custom_instructions'])
    assert actual_input_variables == expected_input_variables

def test_chain_input_if_arg_num_is_correct():
    # chain_input_dictの引数が、(sys_pmtのvariables + human_pmtのvariables)と一致するか
    prompt_class = MakeConversationPrompt()
    actual_args = set(prompt_class.variables("test_search_word", "test_integrated_summary", "nan_j", 20).keys())
    expected_args = set(prompt_class.pmt_tmpl().input_variables) 
    assert actual_args == expected_args
