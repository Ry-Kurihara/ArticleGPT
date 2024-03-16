# 記事の取得（crowler）
export CSE_API_KEY=$(op item get Google_Search_API --fields 認証情報)   
export CSE_ID=$(op item get Google_Search_API --fields CSE_ID)
# 記事内容の生成（interpreter）
export LLM_MODEL_NAME="CLAUDE" # GPT or CLAUDE
export ANTHROPIC_API_KEY=$(op item get Anthropic_API --fields 認証情報)
export OPENAI_API_KEY=$(op item get OpenAI_API --fields 認証情報)
export LANGCHAIN_TRACING_V2=true # langsmithでログを取るかどうか
export LANGCHAIN_API_KEY=$(op item get LangChain_API --fields 認証情報)
export LANGCHAIN_PROJECT="ArticleGPT" # langsmithのUI上でログが格納されるプロジェクト名
# 記事形式の編集（render）
export PA_API_ACCESS_KEY_ID=$(op item get Amazon_PA_API --fields ACCESS_KEY_ID)
export PA_API_SECRET_KEY=$(op item get Amazon_PA_API --fields 認証情報)
export PA_API_PARTNER_TAG=$(op item get Amazon_PA_API --fields PARTNER_TAG)
# 記事の投稿（uploader）
export WP_SITE_URL=$(op item get WordPress_API --fields SITE_URL)
export WP_AUTH_USER=$(op item get WordPress_API --fields ユーザ名)
export WP_AUTH_PASS=$(op item get WordPress_API --fields 認証情報)

# 完了通知
echo 全環境変数をセットしました。警告文等が表示されていなければ完了です。