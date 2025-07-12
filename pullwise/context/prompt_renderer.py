from jinja2 import Environment, FileSystemLoader, select_autoescape
import tiktoken

from pullwise.context.context_builder import ReviewContext

class PromptRenderer:
    def __init__(self, template_dir: str = "templates"):
        self.env = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=select_autoescape()
        )
        self.template = self.env.get_template("review_prompt.j2")

    def render(self, context: ReviewContext) -> str:
        rendered_prompt = self.template.render(
            pr_description=context.pr_description,
            issue_description=context.issue_description,
            chroma_context=context.chroma_context,
            voyage_context=context.voyage_context,
            prior_comments=context.prior_comments,
        )
        return self.truncate_to_token_limit(rendered_prompt)

    def truncate_to_token_limit(self, text: str, max_tokens: int = 4096) -> str:
        enc = tiktoken.encoding_for_model("gpt-4")
        tokens = enc.encode(text)
        if len(tokens) > max_tokens:
            truncated = enc.decode(tokens[:max_tokens])
            return truncated
        return text

    def token_count(self, text: str) -> int:
        enc = tiktoken.encoding_for_model("gpt-4")
        return len(enc.encode(text))
