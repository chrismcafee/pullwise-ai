import os
from typing import List, Dict
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

class ChromaIndexer:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=os.path.expanduser("~/.pullwise/.cache/chroma"))
        self.embedding_fn = OpenAIEmbeddingFunction()

    def index_files(self, files: List[str]) -> Dict:
        collection = self.client.get_or_create_collection(name="codebase", embedding_function=self.embedding_fn)
        indexed_count = 0
        for file_path in files:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            doc_id = os.path.relpath(file_path)
            collection.add(documents=[content], ids=[doc_id])
            indexed_count += 1
        return {"files_indexed": indexed_count, "collection_name": collection.name}
