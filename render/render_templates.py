from jinja2 import Environment, FileSystemLoader
from interpreter.summarize import SummarizedSearchArticle

"""
Objects:
SummarizedSearchArticle → <File Output>
"""

class Format2chSummarizedSearchArticle():
    def __init__(self, article: SummarizedSearchArticle):
        self.env = Environment(loader=FileSystemLoader('.'))
        self.article = article
        self.path = f"render/output/2ch/{article.title}"

    def write_tpl_from_object(self):
        with open(f"{self.path}.html.tpl", "w", encoding="utf-8") as f:
            f.write(self.article.contents)

    def render(self):
        template = self.env.get_template(f"{self.path}.html.tpl")
        output = template.render()
        with open(f"{self.path}.html", 'w', encoding="utf-8") as f:
            f.write(output)

def render_summarized_search_article(article: SummarizedSearchArticle):
    render = Format2chSummarizedSearchArticle(article)
    render.write_tpl_from_object()
    render.render()

def render_specified_tpl_path(path: str, prefix: str = "render/output/2ch/"):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(prefix + path + ".html.tpl")
    output = template.render()
    with open(prefix + path + ".html", 'w', encoding="utf-8") as f:
        f.write(output)



