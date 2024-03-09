# 記事の取得（crowler）
export CSE_API_KEY="your_api_key"
export CSE_ID="your_cse_id"
# 記事内容の生成（interpreter）
export OPENAI_API_KEY="your_openai_api_key"
export LANGCHAIN_TRACING_V2=true # langsmithでログを取るかどうか
export LANGCHAIN_API_KEY=<your-api-key>
export LANGCHAIN_PROJECT="ArticleGPT" # langsmithのUI上でログが格納されるプロジェクト名
# 記事形式の編集（render）
export PA_API_ACCESS_KEY_ID="your_amazon_key_id"
export PA_API_SECRET_KEY="your_amazon_secret_key"
export PA_API_PARTNER_TAG="your_amazon_partner_tag"
# 記事の投稿
export WP_AUTH_USER="your_wp_auth_user"
export WP_AUTH_PASS="your_wp_auth_pass"