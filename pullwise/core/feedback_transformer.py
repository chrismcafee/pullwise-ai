import json

class FeedbackTransformer:
    def normalize_output(self, raw_output: str) -> dict:
        try:
            return json.loads(raw_output)
        except json.JSONDecodeError:
            return {}

    def extract_memory_chunks(self, output: dict) -> list:
        return output.get("suggestions", [])
