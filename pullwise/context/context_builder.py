from pullwise.context.context_model import ReviewContext
from pullwise.ports.memory_store_port import MemoryStorePort

class ContextBuilder:
    def __init__(self, memory_store: MemoryStorePort):
        self.memory_store = memory_store

    def build(self, pr_number: int) -> ReviewContext:
        # Placeholder logic for PR metadata, diff, etc.
        context = ReviewContext(pr_number=pr_number)

        # Memory recall
        query = f"PR #{pr_number}"
        tags = [f"pr:{pr_number}"]
        voyage_context = self.memory_store.recall(query, tags)
        context.voyage_context = voyage_context

        return context
