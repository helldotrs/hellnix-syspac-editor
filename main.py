import os

def is_sudo():
    return geteuid() == 0

print(is_sudo())
