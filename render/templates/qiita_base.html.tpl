{%- for comment in comments -%}
:::note info 
{{ comment.color | color_to_emoji }} {{comment.res}}
:::

{% endfor -%}
