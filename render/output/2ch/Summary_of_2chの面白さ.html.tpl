{%- extends "render/templates/2ch_base.html.tpl" -%}

{%- set search_word = "2chの面白さ" -%}

{%- set comments =[
 {'date': '2023/04/01 00:03:20.55', 'id': 'dCTjJxeka', 'res':'2chは最高やで！', 'color':'blue', 'size':'24px'},
 {'date': '2023/04/01 00:55:20.33', 'id': 'acBTTT7k', 'res':'まあ、面白いスレもあるけど、怖いスレもあるし注意やな', 'color':'red'},
 {'date': '2023/04/02 03:50:20.10', 'id': 'll88J7k', 'res': '2chは一度ハマると抜け出せない魔法の国やで', 'color':'green'},
 {'date': '2023/04/04 11:10:20.04', 'id': 'kk77jLO3', 'res': '俺も2chの面白さにハマったわ。神スレって聞くとさらに興味湧くわ', 'color':'blue'},
 {'date': '2023/04/05 13:20:20.04', 'id': 'll88J7k', 'res': 'でも、気を付けないと個人情報が漏れたり悪質な書き込みに巻き込まれたりすることもあるからね', 'color':'red'},
 {'date': '2023/04/06 15:30:20.04', 'id': 'dCTjJxeka', 'res': 'それはそうやけど、面白いスレはやっぱり見たいもんやろう', 'color':'blue'},
 {'date': '2023/04/08 21:40:20.04', 'id': 'kk77jLO3', 'res': '2chの面白さを伝えるチャンネルってあるんやな！', 'color':'darkviolet'},
 {'date': '2023/04/10 10:00:20.04', 'id': 'acBTTT7k', 'res': 'でも、2chの面白さって自分で探し出さないと見つからないもんやろ。自分で掘り下げていく楽しみがあるからこそ魅力的なんやな', 'color':'green'},
 {'date': '2023/04/12 12:30:20.04', 'id': 'kk77jLO3', 'res': 'そうやな、ワイもいろんなスレを掘り下げてるけど、やっぱり神スレは別格やわ', 'color':'blue'},
 {'date': '2023/04/14 18:20:20.04', 'id': 'acBTTT7k', 'res': '神スレって、一度見たら忘れられないんよな。あの独特な雰囲気とか、ワイは夢中になってしまうわ', 'color':'chocolate'},
 {'date': '2023/04/16 09:10:20.04', 'id': 'dCTjJxeka', 'res': '2chの面白さはやっぱり自分で体験したら分かるもんやな。でも、初めての人は気を付けて探してほしいな', 'color':'green'},
 {'date': '2023/04/18 14:50:20.04', 'id': 'acBTTT7k', 'res': 'それに、2chの面白さは人それぞれ違うから、自分に合ったスレを見つけるのも大事やな', 'color':'green'},
 {'date': '2023/04/20 17:30:20.04', 'id': 'll88J7k', 'res': '2chの面白さは見つけるのが大変やけど、見つけた時の快感はたまらんわ。ワイもこれからまた探し始めるで', 'color':'blue'},
 {'date': '2023/04/22 20:10:20.04', 'id': 'dCTjJxeka', 'res': '2chの面白さを伝えるチャンネルを見たけど、自分で探す方が何倍も楽しいやろうな', 'color':'tan'},
 {'date': '2023/04/24 11:00:20.04', 'id': 'kk77jLO3', 'res': '2chの面白さは自分で探す方がいいけど、初めての人は神スレから入るといいで。ワイも神スレから入ったことがきっかけで、2chの虜になったで', 'color':'blue'},
 ] -%}

{%- set article_review = "2chの面白さは自分で探し出して体験するのが一番やな。でも、初めての人は注意して見つけた方がええで。そんな人には神スレから入るのがおすすめやわ。ワイも神スレから入ったことがきっかけで、2chの虜になったんやで！" %}