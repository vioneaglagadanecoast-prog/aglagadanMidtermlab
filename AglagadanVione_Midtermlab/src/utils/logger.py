import logging
from pathlib import Path


def configure_logging(log_file: Path, level: str = "INFO") -> None:
    """Write logs to a file and display warnings/errors in the terminal."""
    log_file.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(),
        ],
        force=True,
    )
