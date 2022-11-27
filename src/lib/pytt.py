"""Pyttipanna DRY library.

Contains miscellaneous functions that are good enough for re-use but small
enough to not warrant its own library.

Usage:

    from lib import pytt

    pytt.x()

Author: Göran Gustafsson <gustafsson.g@gmail.com>
License: BSD 3-Clause
"""

import os


# Used in "gitpl" and "gitst".
def git_find(path: str, sub_level: bool = False) -> tuple:
    """Find Git repos under directory.

    Checks if ".git" directory exists under sub-directories. Optionally checks
    one sub-level down.

    Arguments:
        path: str containing directory path to search.
        sub_level: bool that sets if sub-level directories should be searched.

    Returns:
        tuple containing Git repo directories sorted by path.
    """

    if sub_level:
        result = []
        for subdir in os.scandir(path):
            if not os.path.isdir(subdir.path):
                continue

            for subdir in os.scandir(subdir.path):
                if os.path.isdir(f"{subdir.path}{os.sep}.git"):
                    result.append(subdir)
    else:
        result = [
            subdir for subdir in os.scandir(path)
            if os.path.isdir(f"{subdir.path}{os.sep}.git")
        ]
    return tuple(sorted(result, key=lambda item: item.path))
