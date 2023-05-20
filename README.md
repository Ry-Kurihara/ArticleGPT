# Draft: ArticleGPT: Automatic article generation tool.

<p align="center">
  <img src="https://github.com/Ry-Kurihara/ArticleGPT/assets/43668533/812ef014-5d37-48c0-95c7-be4c6f96bd80" />
</p>

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
