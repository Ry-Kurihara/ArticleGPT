from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


def prompt_enable_llm_to_summarize_article() -> ChatPromptTemplate:
    sys_template = "あなたは優秀なWeb記事の要約者です。入力された記事内容を元に{word_count}文字程度の文章に要約する天才です。"
    sys_pmt = SystemMessagePromptTemplate.from_template(sys_template)
    human_template = """
        Title: {title}
        {html_contents}
    """
    human_pmt = HumanMessagePromptTemplate.from_template(human_template)
    chat_pmt = ChatPromptTemplate.from_messages([sys_pmt, human_pmt])
    return chat_pmt

def prompt_enable_llm_to_convert_format_to_2ch() -> ChatPromptTemplate:
    with open("interpreter/my_prompts/2ch_system.md", "r") as f:
        file_contents = f.read()
    sys_pmt = SystemMessagePromptTemplate.from_template(file_contents)
    human_template = """
        検索ワード: {search_word}
        要約:
        {integrated_summary}
    """
    human_pmt = HumanMessagePromptTemplate.from_template(human_template)
    chat_pmt = ChatPromptTemplate.from_messages([sys_pmt, human_pmt])
    return chat_pmt