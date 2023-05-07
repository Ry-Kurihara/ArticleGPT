import pytest 
from interpreter.prompt_creater import prompt_enable_llm_to_summarize_article

def test_prompt():
    input_set = {"word_count": 200, "title": "test_title", "html_contents": "test_contents"}
    actual_chat_pmt = prompt_enable_llm_to_summarize_article()
    # assert actual_chat_pmt.format_messages(word_count=300, title="aiueo", html_contents="testes") == "aa"
    assert set(actual_chat_pmt.input_variables) == set(['title', 'word_count', 'html_contents'])