import os

def is_sudo():
    return os.geteuid() == 0

if not is_sudo():
    print("not sudo. limited functionality")
