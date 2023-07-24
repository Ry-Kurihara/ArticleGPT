from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain.prompts import load_prompt


class MakeConversationPrompt:
    # prompt_tamplateとvariablesの組み合わせを定義する
    def pmt_tmpl(self) -> ChatPromptTemplate:
        sys_pmt = SystemMessagePromptTemplate(prompt = load_prompt("interpreter/my_prompts/conversation.json"))
        human_template = """
            検索ワード: {search_word}
            要約:
            {integrated_summary}
        """
        human_pmt = HumanMessagePromptTemplate.from_template(human_template)
        chat_pmt = ChatPromptTemplate.from_messages([sys_pmt, human_pmt])
        return chat_pmt
    
    def variables(self, search_word: str, integrated_summary: str, personality: str = "nan_j", comments_count: int = 10) -> dict[str]:
        return {
            "search_word": search_word,
            "integrated_summary": integrated_summary,
            "personality": get_personality_details(personality),
            "comments_count": comments_count,
        }

class MakeTitlePrompt:
    def pmt_tmpl(self) -> ChatPromptTemplate:
        sys_template = """
            以下の記事本文に関して、記事のタイトルを決定してください。
            文字数は25文字以上55文字以下を厳守してください。
            出力はタイトル文字列のみで大丈夫です。

            タイトル例：
            1. iPhoneでSONYのヘッドホン使うと音劣化したりする？
            2. なぜ、日本のヘッドホンは海外で人気がないのか？
            3. ヘッドホンの音質を変えるイコライザーの使い方
            4. 第3世代AirPodsは実際どんな感じ？ AirPods Proと比較しての音質や機能の違いまとめ
        """
        human_template = """
            記事本文:
            {article_contents}
        """
        human_pmt = HumanMessagePromptTemplate.from_template(human_template)
        sys_pmt = SystemMessagePromptTemplate.from_template(sys_template)
        chat_pmt = ChatPromptTemplate.from_messages([sys_pmt, human_pmt])
        return chat_pmt
    
    def variables(self, article_contents: str) -> dict[str]:
        return {
            "article_contents": article_contents,
        }

def summarize_pmt() -> ChatPromptTemplate:
    sys_template = "あなたは優秀なWeb記事の要約者です。入力された記事内容を元に{word_count}文字程度の文章に要約する天才です。"
    sys_pmt = SystemMessagePromptTemplate.from_template(sys_template)
    human_template = """
        Title: {title}
        {html_contents}
    """
    human_pmt = HumanMessagePromptTemplate.from_template(human_template)
    chat_pmt = ChatPromptTemplate.from_messages([sys_pmt, human_pmt])
    return chat_pmt


def get_personality_details(personality: str) -> str:
    if personality == "nan_j":
        return """
            コメントの全て（最後のレビューコメントを除く）で以下を厳守してください。
            1人称: ワイ
            語尾: [〜やで, 〜やったわ, 〜やないか, 〜やろ, 〜やろか, 〜やろな, 〜やろう, 〜やろうか, 〜やろうな, 〜やろなあ, 〜やろなぁ, 〜やろね, 〜やろねえ, 〜やろねぇ, 〜やろねん, 〜やろねんで]など関西弁に近い語尾を使う
            例文: ほーん、そういうことか。ワイはそういうことは知らんかったんやで。
            性格: おっとり, おもしろい
        """
    elif personality == "intelligence":
        return """
            コメントの全て（最後のレビューコメントを除く）で以下を厳守してください。
            1人称: ワタクシ, このワシ, ワテ
            語尾: [であるのだ, である, 思いまする]など堅い語尾を使う
            例文: ふむふむ、そういうことですか。ワタクシはそういうことは知らなかったのです。
            性格: 真面目, 賢い, 頭が良い, 自尊心が高い
        """
    else:
        raise ValueError(f"board_type: {personality} is not supported.")