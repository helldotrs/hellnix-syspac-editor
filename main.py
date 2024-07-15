import os

def is_sudo():
    return os.geteuid() == 0

print(is_sudo())
