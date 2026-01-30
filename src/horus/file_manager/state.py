from pathlib import Path
import shutil
from . import paths

def copy_dir_contents(src: Path, dst: Path) -> None:

    """copy the src dir contents into the dst dir, overwriting it if neccesary"""

    dst.mkdir(parents=True, exist_ok=True)

    for item in src.iterdir():
        if item.is_file():
            shutil.copy2(item, dst / item.name)
            
def update_target_state(target: str) -> None:

    """copy the targets run data into the state data, overwriting the previous state """

    state_dir = paths.target_state_dir(target)
    run_dir   = paths.target_run_dir(target)

    copy_dir_contents(run_dir, state_dir)