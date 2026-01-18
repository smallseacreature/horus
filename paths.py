from pathlib import Path
import horus.config as config

def target_run_dir(target: str) -> Path:
    return config.DATA_DIR / target / config.DATE_TODAY


def target_state_dir(target: str) -> Path:
    return config.DATA_DIR / target / "state"
