# Write a function or method called find that takes two arguments called path and dir.
# The path argument should accept a relative or absolute path to a directory where the search should start,
# while the dir argument should be the name of a directory that you want to find in the given path.
# Your program should display the absolute paths if it finds a directory with the given name.
# The directory search should be done recursively.

import os


def find_path(path, dir):
    for root, dirs, files in os.walk(path):
        for name in dirs:
            if name == dir:
                print(os.path.abspath(os.path.join(root, name)))


if __name__ == '__main__':
    find_path(path="./tree", dir="python")
