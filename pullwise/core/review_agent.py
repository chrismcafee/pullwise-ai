import os
import json
from datetime import datetime
from pullwise.context.context_builder import ContextBuilder
from pullwise.context.prompt_renderer import PromptRenderer
from pullwise.ports.llm_port import LLMPort
from pullwise.utils.logger import get_logger
from pullwise.settings import Settings
from pullwise.factory.llm_factory import LLMFactory

logger = get_logger("review")

class ReviewAgent:
    def __init__(self, settings: Settings = None, llm: LLMPort = None):
        self.settings = settings or Settings.load()
        self.llm = llm or LLMFactory.from_settings(self.settings)
        self.context_builder = ContextBuilder() # TODO: inject vcs, issue tracker, vector index, memory store adapters
        self.prompt_renderer = PromptRenderer() # TODO: inject template dir

    def review(self, org: str, repo: str, pr_number: int):
        context = self.context_builder.build(pr_number)
        prompt = self.prompt_renderer.render(context)
        output = self.llm.generate(prompt)

        result = json.loads(output)

        timestamp = datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H-%M-%S")
        output_dir = os.path.expanduser(f"~/.pullwise/reviews/{org}/{repo}/{pr_number}/ai/")
        os.makedirs(output_dir, exist_ok=True)
        path = os.path.join(output_dir, f"review-{timestamp}.json")
        with open(path, "w") as f:
            json.dump(result, f, indent=2)

        logger.info(f"Saved AI review to {path}")
