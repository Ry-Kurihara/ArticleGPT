<p align="center">
  <img src="https://github.com/Ry-Kurihara/ArticleGPT/assets/43668533/812ef014-5d37-48c0-95c7-be4c6f96bd80" alt="ArticleGPT" />
</p>

# Simple discription
記事の自動生成ツールです。Enterボタン1ポチで特定の話題に対するまとめ記事を生成できます。  
※ 開発中のため動作しない環境が多いと思われます。コードの参考程度でお願いしますmm

# Instruction
https://qiita.com/Ryku/items/939287c5f500c60dbac9

# How to use?
```sh 
python main.py 今日の天気
```

# How to test?
## ALL
```sh 
python -m pytest -v ./
```

## Each module
```sh 
python -m pytest -v crowler/
```

```sh 
python -m pytest -v interpreter/
```

```sh
python -m pytest -v render/
```

# Features
`crowler`、`interpreter`、`render`の主要3モジュールの構成で動いています。

- crowler
  - コマンドライン引数で指定されたワードを元に、Google検索結果を取得します。
  - 上位X件の結果を取得し、各記事のHTML文章を見やすい形に解析して次の`interpreter`モジュールに渡します。
- interpreter
  - `crowler`モジュールから渡されたHTML文章を元に、LangChainを使用して会話形式の文章を生成します。
  - 生成された文章は、`render`モジュールに渡されます。
- render
  - `interpreter`モジュールから渡された文章を元に、Jinja2を使用して各種サイトに投稿できる状態のHTML文章を生成します。

# Ingenuity
- BeautifulSoup
  - `crowler`モジュールでは、HTML文章の解析にBeautifulSoupを使用しています。
- LangChain
  - `interpreter`モジュールでは、LangChainが使用されています。 
  - 直接APIを叩かずにLangChainを通して実装することで、拡張性を高めています。
- Jinja2
  - テンプレートエンジンとして`render`モジュールにJinja2を使用しています。
  - `render`モジュールのカスタマイズ次第で、さまざまな出力形式に対応できます。

# Contact
```
　／￣＼
○ ／￣￣￣＼ヘ
　 /・　 ・　 ＼>
／￣￣￣＼　　 Ｖ|
｜ ――― ｜　　｜|
＼＿＿＿／　　 ∧|
　　＼　　　　／〉
　　　￣￣￣￣￣
　　ヽ(´･ω･)ﾉ
　　　 |　 /
　　　 UU
うっせぇ、アンコウ投げんぞ!
```

https://twitter.com/ryku_data