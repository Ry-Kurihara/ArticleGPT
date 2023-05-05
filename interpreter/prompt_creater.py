from langchain.prompts import PromptTemplate

def prompt_enable_llm_to_convert_format_to_2ch() -> PromptTemplate:
    with open("interpreter/my_prompts/2ch_generation.md", "r") as f:
        file_contents = f.read()
    print(f"file_cont: {file_contents}")
    input_variables = ["search_word", "integrated_summary"]
    return PromptTemplate(input_variables=input_variables, template=file_contents)

def prompt_enable_llm_to_summarize_article() -> PromptTemplate:
    prompt = PromptTemplate(
        input_variables=["title", "html_contents", "word_count"],
        template="""
        以下の内容を{word_count}文字程度に要約してください。

        ```
        Title: {title}
        {html_contents}
        ```
        """
    )
    return prompt