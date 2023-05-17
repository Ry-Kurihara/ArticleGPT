<div class="information-box">
    この記事は{{ search_word }}に関する記事です。
    以下、皆さんの反応です。
</div>

{% for comment in comments %}
<div class="t_h" ><div class="mtmks">{{loop.index + 100}}: <span style="color: green; font-weight: bold;">イヤホン速報</span> <span style="color: gray;"> {{ comment.date }} ID:{{ comment.id }}</span></div></div>
<div class="t_b" style="font-weight:bold;margin-bottom:90px;margin-top:16px;color:{{comment.color|default('black')}};font-size:{{comment.size|default('18px')}};">{{comment.res}}</div><br/>
{%- endfor %}

<hr>

<div class="speech-wrap sb-id-11 sbs-stn sbp-l sbis-cb cf">
<div class="speech-person">
<figure class="speech-icon"><img class="speech-icon-image" src="https://earsoku.com/wp-content/uploads/2020/03/profile.png" alt="" /></figure>
</div>
<div class="speech-balloon">
{{ article_review }}
</div>
</div>