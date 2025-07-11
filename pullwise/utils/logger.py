import logging
import os
from datetime import datetime
from pathlib import Path

from pullwise.config.paths import get_log_path

class LoggerFactory:
    @staticmethod
    def create_logger(org: str, repo: str, pr_number: int, command: str, verbose: bool = False) -> logging.Logger:
        log_path = get_log_path(org, repo, pr_number, command)
        Path(log_path).parent.mkdir(parents=True, exist_ok=True)

        logger = logging.getLogger(f"{org}_{repo}_{pr_number}_{command}")
        logger.setLevel(logging.DEBUG if verbose else logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # File handler
        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Optional stdout handler
        if verbose:
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            logger.addHandler(stream_handler)

        return logger
