from pullwise.ports.memory_store_port import MemoryStorePort

class VoyageMemoryStore(MemoryStorePort):
    def __init__(self, cache_dir):
        self.cache_dir = cache_dir

    def query(self, query: str, repo: str):
        return []

    def save(self, org: str, repo: str, pr_number: int, content: str):
        pass
