import os
from typing import List
from chromadb import Client
from chromadb.config import Settings
from pullwise.ports.vector_index_port import VectorIndexPort
from pullwise.config.paths import get_cache_dir

class ChromaIndexer(VectorIndexPort):
    def __init__(self):
        self.cache_path = get_cache_dir("chroma")
        os.makedirs(self.cache_path, exist_ok=True)
        self.client = Client(Settings(persist_directory=self.cache_path))
        self.collection = self.client.get_or_create_collection("codebase")

    def index_repo(self, repo_path: str, language_filter: str = None):
        for root, _, files in os.walk(repo_path):
            for file in files:
                if not file.endswith(".py") and language_filter == "python":
                    continue
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                    self.collection.add(
                        documents=[content],
                        metadatas=[{"path": path}],
                        ids=[path]
                    )
                except Exception as e:
                    print(f"Failed to index {path}: {e}")

    def query(self, query: str, top_k: int = 5) -> List[dict]:
        results = self.collection.query(query_texts=[query], n_results=top_k)
        return [
            {"path": doc["path"], "content": doc["document"]}
            for doc in zip(results["metadatas"][0], results["documents"][0])
        ]

