class ContextBuilder:
    def build(self, pr_number: int):
        return {
            "pr_number": pr_number,
            "pr_description": "This is a placeholder PR description",
            "issue_description": "Optional linked issue",
            "code_context": [],
            "voyage_memory": [],
            "prior_comments": []
        }
