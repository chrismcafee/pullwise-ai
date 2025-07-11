import os
from typing import List

def scan_codebase(base_path: str, language: str = None) -> List[str]:
    extensions = {
        "python": [".py"],
        "javascript": [".js", ".jsx"],
        "typescript": [".ts", ".tsx"]
    }
    ext_filter = extensions.get(language.lower(), None) if language else None
    file_list = []
    for root, _, files in os.walk(base_path):
        for fname in files:
            if not fname.startswith("."):
                fpath = os.path.join(root, fname)
                if not ext_filter or any(fname.endswith(ext) for ext in ext_filter):
                    file_list.append(fpath)
    return file_list
