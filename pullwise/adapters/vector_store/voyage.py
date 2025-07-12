import os
import json
from typing import List, Dict
from pullwise.ports.memory_store_port import MemoryStorePort

class VoyageAdapter(MemoryStorePort):
    # todo: move base_dir to path helper
    def __init__(self, base_dir: str = "~/.pullwise/.cache/voyage/"):
        self.base_dir = os.path.expanduser(base_dir)
        os.makedirs(self.base_dir, exist_ok=True)

    def _get_repo_path(self, repo: str) -> str:
        path = os.path.join(self.base_dir, repo)
        os.makedirs(path, exist_ok=True)
        return path

    def save_memory(self, pr_id: str, context, ai_output: str) -> None:
        repo = context.repo
        path = self._get_repo_path(repo)
        file_path = os.path.join(path, f"{pr_id}.json")
        with open(file_path, "w") as f:
            json.dump({"context": context.to_dict(), "output": ai_output}, f)

    def recall(self, prompt: str, tags: List[str]) -> List[str]:
        repo = tags[0] if tags else ""
        path = self._get_repo_path(repo)
        results = []
        for fname in os.listdir(path):
            if fname.endswith(".json"):
                with open(os.path.join(path, fname)) as f:
                    data = json.load(f)
                    results.append(data["output"])
        return results
