import requests
import os

"""
Objects:
<File Name> → Reading... → <HTTP Upload>
"""

class WpInfos():
    def __init__(self) -> None:
        self.SITE_URL = "https://earsoku.com"
        self.API_URL = f"{self.SITE_URL}/wp-json/wp/v2/posts"
        self.AUTH_USER = os.getenv("WP_AUTH_USER")
        self.AUTH_PASS = os.getenv("WP_AUTH_PASS")


def print_some_articles(print_num: int = 5):
    wp_infos = WpInfos()
    response = requests.get(wp_infos.API_URL).json()
    for i, data in enumerate(response[:print_num]):
        print(f'{i+1}: {data["title"]["rendered"]}, {data["date"]}, {data["modified"]}')


def upload_draft_to_wp(html_file_name: str):
    wp_infos = WpInfos()
    with open(html_file_name, 'r') as f:
        html_content = f.read()

    title = os.path.splitext(os.path.basename(html_file_name))[0]
    post_data = {
        'title': title,
        'content': html_content,
        'status': 'draft'
    }
    print(f"title: {title}")
    response = requests.post(wp_infos.API_URL, auth=(wp_infos.AUTH_USER, wp_infos.AUTH_PASS), json=post_data)

    if response.status_code == 201:
        print('記事をアップロードしました！')
    else:
        print('記事のアップロードに失敗しました。')
        print(f"エラー内容: {response.text}")


if __name__ == "__main__":
    print_some_articles()
    upload_draft_to_wp("render/output/2ch/Summary_of_momentum4 接続安定性 不満点.html")