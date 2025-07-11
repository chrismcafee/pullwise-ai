import os
import logging
from datetime import datetime

def get_logger(command: str):
    timestamp = datetime.now(datetime.timezone.utc).strftime("%Y_%m_%d")
    log_dir = os.path.expanduser("~/.pullwise/logs/")
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, f"{timestamp}_org_repo_pr1_{command}.log")

    logger = logging.getLogger(command)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(log_path)
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
