from pathlib import Path
import horus.config as config 

DATA_DIR = Path("./data")

def target_run_dir(target: str) -> Path:
    """generate path object for location of new scan data"""
    return DATA_DIR / target / str(config.DATE_TODAY)

def target_state_dir(target: str) -> Path:
    """generate path object for location of the most recent scan data"""
    return DATA_DIR / target / "state"
