from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain.prompts import load_prompt

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

# プロンプトを呼び出す時点で入れるVariablesが確定していて欲しい
# 2ch_board_typeを入れたら適切なsentence_typeが挿入されるようにしたい
class Prompt2chBase:
    def prompt_enable_llm_to_convert_format_to_2ch(self) -> ChatPromptTemplate:
        sys_pmt = SystemMessagePromptTemplate(prompt = load_prompt("interpreter/my_prompts/2ch_system.json"))
        print(f"sys_pmt: {sys_pmt}")
        human_template = """
            検索ワード: {search_word}
            要約:
            {integrated_summary}
        """
        human_pmt = HumanMessagePromptTemplate.from_template(human_template)
        chat_pmt = ChatPromptTemplate.from_messages([sys_pmt, human_pmt])
        return chat_pmt
    
    def describe_details_of_board_type(self, board_type: str) -> str:
        if board_type == "nan_j":
            return """
                コメントの全てで以下を厳守してください。
                1人称: ワイ
                語尾: [〜やで, 〜やったわ, 〜やないか, 〜やろ, 〜やろか, 〜やろな, 〜やろう, 〜やろうか, 〜やろうな, 〜やろなあ, 〜やろなぁ, 〜やろね, 〜やろねえ, 〜やろねぇ, 〜やろねん, 〜やろねんで]など関西弁に近い語尾を使う
                例文: ほーん、そういうことか。ワイはそういうことは知らんかったんやで。
                性格: おっとり, おもしろい
            """
        elif board_type == "intelligence":
            return """
                コメントの全てで以下を厳守してください。
                1人称: ワタクシ, このワシ, ワテ
                語尾: [であるのだ, である, 思いまする]など堅い語尾を使う
                例文: ふむふむ、そういうことですか。ワタクシはそういうことは知らなかったのです。
                性格: 真面目, 賢い, 頭が良い, 自尊心が高い
            """
        else:
            raise ValueError(f"board_type: {board_type} is not supported.")
    
    def chain_input_dict(self, search_word: str, integrated_summary: str, board_type: str) -> dict[str]:
        return {
            "search_word": search_word,
            "integrated_summary": integrated_summary,
            "board_type_details": self.describe_details_of_board_type(board_type)
        }
