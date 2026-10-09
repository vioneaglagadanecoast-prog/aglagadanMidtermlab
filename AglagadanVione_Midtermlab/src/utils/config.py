import json
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = PROJECT_ROOT / "config" / "config.json"


def load_config() -> dict[str, Any]:
    defaults: dict[str, Any] = {
        "data_file": "data/students.json",
        "log_file": "logs/app.log",
        "log_level": "INFO",
        "app_name": "Student Information System",
    }
    try:
        with CONFIG_PATH.open("r", encoding="utf-8") as file:
            configured = json.load(file)
        defaults.update(configured)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Warning: using default configuration ({exc}).")
    return defaults


def resolve_project_path(relative_path: str) -> Path:
    return PROJECT_ROOT / relative_path
