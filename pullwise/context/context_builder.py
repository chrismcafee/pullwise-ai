from pullwise.context.context_model import ReviewContext, PullRequestMetadata, IssueMetadata, CodeContext
from datetime import datetime

class ContextBuilder:
    def __init__(self, vcs_port, issue_tracker_port, vector_index_port, memory_store_port):
        self.vcs = vcs_port
        self.issues = issue_tracker_port
        self.vector = vector_index_port
        self.memory = memory_store_port

    def build(self, pr_number: int) -> ReviewContext:
        # 1. Fetch PR metadata
        pr_meta = self.vcs.get_pr_metadata(pr_number)
        pr = PullRequestMetadata(
            number=pr_number,
            title=pr_meta["title"],
            description=pr_meta["description"],
            author=pr_meta["author"],
            base_branch=pr_meta["base"],
            head_branch=pr_meta["head"],
        )

        # 2. Fetch diff files
        diff_files_raw = self.vcs.get_pr_diff(pr_number)
        diff_files = [DiffFile(filename=f["file"], diff=f["diff"]) for f in diff_files_raw]

        # 3. Fetch linked issue (if any)
        issue = None
        if "issue_key" in pr_meta:
            issue_data = self.issues.get_issue(pr_meta["issue_key"])
            issue = IssueMetadata(
                key=issue_data["key"],
                summary=issue_data["summary"],
                description=issue_data.get("description"),
            )

        # 4. Fetch vector context from Chroma
        vector_context = []
        for f in diff_files:
            chunks = self.vector.query(filename=f.filename, top_k=3)
            for chunk in chunks:
                vector_context.append(CodeContext(filename=f.filename, snippet=chunk))

        # 5. Fetch voyage memory (prior PR reviews)
        voyage_context = self.memory.recall(prompt=pr.title + " " + pr.description, tags=[pr_meta["repo"]])

        # 6. Fetch prior comments (if available)
        prior_comments = self.vcs.get_review_comments(pr_number)

        return ReviewContext(
            pr=pr,
            diff_files=diff_files,
            linked_issue=issue,
            chroma_context=vector_context,
            voyage_context=voyage_context,
            prior_comments=prior_comments
        )
