#preflight.py

from shutil import which
import horus.config as config
from pathlib import Path

def check_command(command):
    """ return T/F on commands existence """
    if which(command) == None:
        return False
    else:
        return True

def check_tools():
    security_tools = config.security_tools
    for tool in security_tools:
        if check_command(tool) != True:
            print(f"[X] FATAL ERROR: {tool} is not found, install or add to PATH")
            exit()

def check_defaults():
    if config.contact_header == "X-Contact: example@email.com":
        print("Please change the contact header, located at the top of the source code")
        exit()

#TODO check for .env

def preflight_checks(DEBUG = False):
    if DEBUG:
        print("Starting preflight checks")

    check_tools()
    check_defaults()

    if DEBUG:
        print("Preflight checks GOOD")