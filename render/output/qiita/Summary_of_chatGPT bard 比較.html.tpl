{%- extends 'render/templates/qiita_base.html.tpl' -%}

{%- set search_word = "chatGPT bard 比較" -%}

{%- set comments =[
 {'date': '2023/06/01 14:20:36.22', 'id': 'dCTjJxeka', 'res':'ChatGPTとBardの違いって何ですか？', 'color':'black', 'size':'18px'},
 {'date': '2023/06/01 14:25:10.80', 'id': 'acBTTT7k', 'res':'ChatGPTは日本でも利用可能で、Microsoft社が運営するBingを活用しています。BardはGoogle社の対話型AIで、日本でのリリースはまだ未定です。', 'color':'black'},
 {'date': '2023/06/01 14:30:45.30', 'id': 'll88J7k', 'res': 'Bardは最新情報に基づいて回答でき、Google検索と連動していますね。', 'color': 'black'},
 {'date': '2023/06/01 14:35:20.50', 'id': 'kk77jLO3', 'res': 'ChatGPTはGenerative Pre-trained Transformer、BardはLanguage Model for Dialogue Applicationsがベースになっているそうですね。', 'color':'black'},
 {'date': '2023/06/01 14:40:15.70', 'id': 'dCTjJxeka', 'res': 'どちらが優れているかは何ですか？', 'color':'black', 'size':'18px'},
 {'date': '2023/06/01 14:45:05.10', 'id': 'acBTTT7k', 'res': 'それは使い分けによると思いますが、Bardはストーリー性のある回答を提供することが多いそうですよ。', 'color': 'black'},
 {'date': '2023/06/01 14:50:25.80', 'id': 'll88J7k', 'res': '一方、ChatGPTは箇条書きで回答することが多いようですね。', 'color': 'black'},
 {'date': '2023/06/01 14:55:10.20', 'id': 'kk77jLO3', 'res': '何か具体的な例があったら教えてください。', 'color':'black', 'size':'18px'},
 {'date': '2023/06/01 15:00:40.10', 'id': 'dCTjJxeka', 'res': 'Bardに「ロボスタ」というWebマガジンを紹介した場合、どのような回答になるのでしょうか？', 'color':'black', 'size':'18px'},
 {'date': '2023/06/01 15:05:15.70', 'id': 'acBTTT7k', 'res': 'ロボスタについては、ICTの最新情報に特化したロボット情報WEBマガジンです。', 'color': 'black'},
 ] -%}

{%- set article_review = "ChatGPTとBardの違いについて詳しく知ることができた貴重な記事でした。両者の特徴や性能についてわかりやすく解説されており、使い分けの参考になりました。" %}