import os, time
from amazon_paapi import AmazonApi
from amazon_paapi.models import SearchResult


def _create_amazon_instance_from_env() -> AmazonApi:
    access_key = os.environ['PA_API_ACCESS_KEY_ID']
    secret_key = os.environ['PA_API_SECRET_KEY']
    partner_tag = os.environ['PA_API_PARTNER_TAG']
    country = 'JP'
    thorottling = 1.5 # Rate limit：1リクエスト/秒 & 8640リクエスト/日, 参考：https://webservices.amazon.com/paapi5/documentation/troubleshooting/api-rates.html
    return AmazonApi(access_key, secret_key, partner_tag, country, thorottling=thorottling)


def process_item(item: str) -> str:
    # 商品名からアマゾンPA-APIのSearchItemsオペレーションを使用してASINを取得し、WPのAmazonJSプラグインのショートコードを生成する
    amazon = _create_amazon_instance_from_env()
    time.sleep(2) # Rate limit対策
    search_result: SearchResult = amazon.search_items(keywords=item, item_count=5) # HACK: prime出品のみ等、信頼度の高い商品のみに絞りたい
    first_item_asin = search_result.items[0].asin
    return f"[amazonjs asin='{first_item_asin}' locale='JP' title={item}]"


# デバッグ用
def _debug_search_result(search_result: SearchResult):
    result_items = search_result.items
    for i, item in enumerate(result_items):
        print(f"{i}: {item.item_info.title}")


if __name__ == "__main__":
    # デバッグ用：python -m render.external_processor
    # プロダクトでは関数呼び出しから使うため、ここは実行されない
    process_item('AZ80')