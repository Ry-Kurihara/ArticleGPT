from langchain.prompts import PromptTemplate

def create_template_enable_llm_to_make_articles() -> PromptTemplate:
    input_variables = ["search_word", "integrated_summary"]
    with open("article_creater/my_prompts/summarize_2ch.html", "r") as f:
        file_contents = f.read()
    print(f"file_cont: {file_contents}")
    return PromptTemplate(input_variables=input_variables, template=file_contents)

prompt_summarize_each_article: PromptTemplate = PromptTemplate(
    input_variables=["title", "html_contents"],
    template="""
    以下の内容を300文字程度に要約してください。

    ```
    Title: {title}
    {html_contents}
    ```
    """
)