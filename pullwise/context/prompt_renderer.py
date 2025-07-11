import jinja2
from pathlib import Path
from tiktoken import encoding_for_model

class PromptRenderer:
    def __init__(self):
        templates_dir = Path(__file__).parent.parent / 'templates'
        loader = jinja2.FileSystemLoader(templates_dir)
        self.env = jinja2.Environment(loader=loader)

    def render(self, context):
        template = self.env.get_template("review_prompt.j2")
        return template.render(context)

    def token_count(self, text: str) -> int:
        enc = encoding_for_model("gpt-4")
        return len(enc.encode(text))
