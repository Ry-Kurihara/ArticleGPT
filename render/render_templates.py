from jinja2 import Environment, FileSystemLoader
from interpreter.convert import BlogPosting

"""
Objects:
BlogPosting → <File Output>
"""

class BaseFormatter():
    def __init__(self, output_dir: str) -> None:
        self.env = Environment(loader=FileSystemLoader('.'))
        self.output_dir = f"render/output/{output_dir}"
        self.env.globals['process_item'] = self.process_item

    def process_item(self, item: str) -> str:
        asin = 'amazon_asin_'
        return asin + item

    def write_tpl_from_object(self, article: BlogPosting, file_name: str):
        with open(f"{self.output_dir}/{file_name}.html.tpl", "w", encoding="utf-8") as f:
            f.write(article.contents)

    def render(self, file_name: str):
        template = self.env.get_template(f"{self.output_dir}/{file_name}.html.tpl")
        output = template.render()
        with open(f"{self.output_dir}/{file_name}.html", 'w', encoding="utf-8") as f:
            f.write(output)

class SecondChFormatter(BaseFormatter):    
    def write_tpl_from_object(self, article: BlogPosting, file_name: str):
        with open(f"{self.output_dir}/{file_name}.html.tpl", "w", encoding="utf-8") as f:
            f.write("{%- extends 'render/templates/2ch_base.html.tpl' -%}\n\n")
            f.write(article.contents)


class QiitaFormatter(BaseFormatter):
    def __init__(self, output_dir: str) -> None:
        super().__init__(output_dir)
        self.env.filters["color_to_emoji"] = self.convert_color_to_emoji

    def write_tpl_from_object(self, article: BlogPosting, file_name: str):
        with open(f"{self.output_dir}/{file_name}.html.tpl", "w", encoding="utf-8") as f:
            f.write("{%- extends 'render/templates/qiita_base.html.tpl' -%}\n\n")
            f.write(article.contents)

    @staticmethod
    def convert_color_to_emoji(color):
        if color == "black":
            return ":smiley:"
        elif color == "blue":
            return ":laughing:"
        elif color == "red":
            return ":cold_sweat:"
        elif color == "green":
            return ":joy:"
        elif color == "chocolate":
            return ":angry:"
        elif color == "tan":
            return ":scream:"
        elif color == "darkviolet":
            return ":neckbeard:"
        else:
            return ":smiley:"


def render_summarized_search_article(article: BlogPosting):
    render = SecondChFormatter("2ch") # CHANGE: 生成したい記事タイプによってここを変更する運用にしている
    file_name = article.title
    render.write_tpl_from_object(article, file_name)
    render.render(file_name)