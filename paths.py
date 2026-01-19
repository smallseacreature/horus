from pathlib import Path
import horus.config as config

def target_run_dir(target: str) -> Path:
    """generate path object for location of new scan data"""
    return config.DATA_DIR / target / config.DATE_TODAY


def target_state_dir(target: str) -> Path:
    """generate path object for location of the most recent scan data"""
    return config.DATA_DIR / target / "state"
