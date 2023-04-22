import openai
import os
from dataclasses import dataclass

# OpenAI APIキーを環境変数から取得する
openai.api_key = os.getenv("OPENAI_API_KEY")

@dataclass
class PromptPrefix:
    summarlize: str 
    add_role: str

    def __init__(self, custom_summarlize: str = "", custom_add_role: str = "") -> None:
        if not custom_summarlize:
            self.summarlize = "次の文章を200文字程度で要約してください。\n"
        else:
            self.summarlize = custom_summarlize
        if not custom_add_role:
            self.add_role = "あなたは猫です。これ以降の会話では常に語尾には「にゃ」を付けてください。\n"
        else:
            self.add_role = custom_add_role

def generate_text(src_string: str, prefixs*) -> str:
    model_engine = "gpt-3.5-turbo"
    prompt = "".join(prefixs).join(src_string)
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024, # GPT3が生成する文章の最大単語数
        n=1,
        stop=None,
        temperature=0.7, # 高いほどGPT3が生成する文章の多様性？が上がるらしい（0〜1.0）
    )
    # 生成された文章を取得する
    generated_text = response.choices[0].text.strip()
    return generated_text

def summerlize_articles(content_html: str) -> str:
    prompt_prefix = PromptPrefix()
    response_text = generate_text(content_html, prompt_prefix.summarlize)
    return response_text