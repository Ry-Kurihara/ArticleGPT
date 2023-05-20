{%- extends "render/templates/2ch_base.html.tpl" -%}

{%- set search_word = "AirPods Pro" -%}

{%- set comments =[
 {'date': '2023/06/01 08:23:20.55', 'id': 'dCmR8Jk', 'res':'AirPods Proのノイズキャンセリングは最高だよ！', 'color':'blue', 'size':'20px'},
 {'date': '2023/06/01 09:45:20.33', 'id': 'acBTR7k', 'res':'でも、値段は高すぎるんじゃ…', 'color':'red'},
 {'date': '2023/06/02 10:12:20.10', 'id': 'll88J7k', 'res': '1世代から2世代に買い替えた人いる？何が変わったのか気になる！'},
 {'date': '2023/06/03 15:10:20.04', 'id': 'kk77jLO3', 'res': '充電ケースにストラップ穴とスピーカーが搭載されたって聞いたけど、使い勝手はどうなの？'},
 {'date': '2023/06/05 09:20:20.04', 'id': 'll88J7k', 'res': '探すアプリで正確に探すことができるのは便利だと思う！', 'size': '24px'},
 {'date': '2023/06/05 11:30:20.04', 'id': 'mmDfJ7k', 'res': 'AirPods Proはバッテリー寿命が2年で交換する必要があるって聞いたけど、Apple Careに入ると1回は無料で交換してくれるんだよね！', 'color':'green'},
 {'date': '2023/06/06 13:45:20.04', 'id': 'll88J7k', 'res': 'Apple Careって加入する価値あるのかな？', 'size': '20px'},
 {'date': '2023/06/07 16:40:20.04', 'id': 'mmDfJ7k', 'res': 'AirPods Proだけでなく、iPadやiPhoneでも使えるし、万が一のトラブルに備えてApple Careに加入するのはおすすめだよ！', 'color':'green'},
 {'date': '2023/06/08 19:20:20.04', 'id': 'll88J7k', 'res': 'なるほど！Apple製品を愛用している人はApple Careに加入しておいた方が良さそうだね！', 'size': '24px'},
 {'date': '2023/06/09 22:00:20.04', 'id': 'mmDfJ7k', 'res': 'そうだね！Apple Careに加入すると、掃除もしてくれるし、Apple Storeでの購入には分割払いやApple Trade Inなどの特典があるから、かなりお得だよ！', 'color':'green', 'size': '24px'},
 {'date': '2023/06/10 08:30:20.04', 'id': 'll88J7k', 'res': 'ほんとだ！Apple Careってこんなにお得なんだ！', 'size': '20px'},
 {'date': '2023/06/10 11:40:20.04', 'id': 'bb8dJ7k', 'res': 'AirPods Proってハイレゾには対応してないんだよね…', 'color':'red'},
 {'date': '2023/06/12 14:30:20.04', 'id': 'll88J7k', 'res': 'でも、ノイキャン性能はBose QuietComfort Earbuds IIと比較しても高いっていうから、音質重視じゃない人にはおすすめだと思う！', 'size': '24px'},
 {'date': '2023/06/13 17:20:20.04', 'id': 'bb8dJ7k', 'res': 'それはそうだね！オーディオ製品はお試しレンタルがあるから、まずはレンタルしてみるのもいいかもしれないね', 'color':'green', 'size': '24px'},
 {'date': '2023/06/14 21:10:20.04', 'id': 'll88J7k', 'res': 'そうだね！レンタルしてから購入を決めるのもいい方法だね！', 'size': '20px'},
 ] -%}

{%- set article_review = "AirPods Pro第2世代についての情報がまとまっていて良かった！Apple Careに入るとかなりお得だし、値段は高いけどノイキャン性能は高いから音質よりも快適性を重視する人にはおすすめだね！" %}