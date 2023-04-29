from langchain.prompts import PromptTemplate

prompt_enable_llm_to_make_articles: PromptTemplate = PromptTemplate(
    input_variables=["search_word", "integrated_contents"],
    template="""
    以下は{search_word}を検索した際に表示される上位3記事の要約文章です。
    ```
    {integrated_contents}
    ```

    これらの情報をもとに、{search_word}を説明する記事をmarkdawn形式で記述してください。
    記事の形式としては以下を参考にしてください。
    参考形式:
    # <Title>

    ## <Headline1>
    Write a overview about {search_word}.

    ## <Headline2>
    Describe the distinctive aspects of {search_word}.
    """
    ,
)

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