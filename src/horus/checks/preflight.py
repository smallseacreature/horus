#preflight.py

from shutil import which

def check_command(command):
    """ return T/F on commands existence """
    if which(command) == None:
        return False
    else:
        return True

def program_start(security_tools: list[str], contact_header: str):

    """ Check to see program can run successfully, and if defaults have been changed"""
    print("\nH O R U S\n")

    for tool in security_tools:
        if check_command(tool) != True:
            print(f"{tool} is not found, install or add to PATH")
            exit()

    if contact_header == "X-Contact: example@email.com":
        print("Please change the contact header, located at the top of the source code")
        exit()

#TODO CHECK IF DATA FOLDER EXISTS