"""Pyttipanna DRY module.

Contains miscellaneous functions that are good enough for re-use but small
enough to not warrant its own module.

Usage:

    from lib.pytt import x

Author: Göran Gustafsson <gustafsson.g@gmail.com>
License: BSD 3-Clause
"""

import os


# Used in "gitpl" and "gitst".
def git_find(dir_: str, sub_level: bool = False) -> tuple:
    """Find Git repos under directory.

    Checks if ".git" directory exists under sub-directories. Optionally checks
    one sub-level down.

    Arguments:
        dir_: os.DirEntry containing directory to search.
        sub_level: bool that sets if sub-level directories should be searched.

    Returns:
        tuple containing Git repo directories sorted by path.
    """

    result = []
    if sub_level:
        for subdir in os.scandir(dir_):
            if not os.path.isdir(subdir.path):
                continue

            for subdir2 in os.scandir(subdir.path):
                if os.path.isdir(f"{subdir2.path}{os.sep}.git"):
                    result.append(subdir2)
    else:
        for subdir in os.scandir(dir_):
            if os.path.isdir(f"{subdir.path}{os.sep}.git"):
                result.append(subdir)
    return tuple(sorted(result, key=lambda l: l.path))
