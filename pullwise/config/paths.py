import os
from datetime import datetime

def get_repo_root():
    return os.getcwd()

def get_cache_dir(component: str):
    return os.path.expanduser(f"~/.pullwise/.cache/{component}")

def get_log_path(org, repo, pr_number, command):
    timestamp = datetime.now().strftime("%Y_%m_%d")
    return os.path.expanduser(
        f"~/.pullwise/logs/{timestamp}_{org}_{repo}_pr{pr_number}_{command}.log"
    )
