def process_item(item: str) -> str:
    # 商品名からアマゾンPA-APIのSearchItemsオペレーションを使用してASINを取得する
    asin = 'amazon_asin_'
    return asin + item