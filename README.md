# Draft: ArticleGPT: Automatic article generation tool.

![articlegpt-log1](https://user-images.githubusercontent.com/43668533/235345177-3c42ca4a-f268-4393-9070-69800f93faf8.png)

## Simple discription
記事の自動生成ツールです。Enterボタン1ポチで特定の話題に対するまとめ記事を生成できます。

# DEMO

# Features

# How to use

# Technical ingenuity
- LangChain
  - 直接APIを叩かずにLangChainを通して実装することで、拡張性を高めています。
- Jinja2
  - 記事生成のテンプレートを一旦GPTに読み込ませる必要があり、ここでAPI使用料が嵩みがち。
  - そこでJinja2を使用することで読み込ませる量を減らしている。

# Please Contact me
