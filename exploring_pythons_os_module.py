import os

def list_directory_contents(path, directory):
    if path in directory:
        print(os.listdir())
    else:
        print("Invalid")