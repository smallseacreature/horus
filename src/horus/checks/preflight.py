#preflight.py

from shutil import which
import horus.config as config
from pathlib import Path
import os
from dotenv import load_dotenv
import sys

def terminal_command_valid(command: str) -> bool:

    """ return T/F on a terminal commands existence """

    if which(command) == None:
        return False
    else:
        return True

def preflight_check_tools() -> None:

    """ Reads a list of terminal commands from config and checks each for validity, raises error if not tool"""

    missing_tools = []

    #read list from config
    required_tools = config.required_tools

    #check each tool
    for tool in required_tools:
        if not terminal_command_valid(tool):
            missing_tools.append(tool)

    #output missing tools
    if missing_tools:
        for tool in missing_tools:
            print(f"[X] {tool} not found, install or add to PATH", file=sys.stderr)
        sys.exit(1)
           
def preflight_check_defaults()  -> None:

    """ Checks the default values that must be changed"""

    if config.contact_header == "X-Contact: example@email.com":
        print(
            "Please change the contact header, located in config.py",
            file=sys.stderr
            )
        sys.exit(1)
    
    if config.user_agent_header == "User-Agent: ":
        print(
            "Please change the user agent header, located in config.py. ie: User-Agent:HackerOne-Research", 
            file=sys.stderr
        )
        sys.exit(1)

def preflight_check_env()  -> None:

    """ Checks to make sure user created an env file and changed the values"""

    env_path = Path(".env")

    error = ".env file is required. Please copy the example and change the values"


    if not env_path.is_file():
        print(error, file=sys.stderr)
        sys.exit(1)

    load_dotenv(dotenv_path=env_path)
    WEBHOOK = os.getenv("DISCORD_WEBHOOK_URL")
    if not WEBHOOK:
        print(error, file=sys.stderr)
        sys.exit(1)
     

def run_preflight_checks() -> None:

    """ Runs all preflight checks """

    preflight_check_tools()
    preflight_check_defaults()
    preflight_check_env()
