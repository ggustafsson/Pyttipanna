"""Terminal colors module.

Contains terminal color and attribute values for convenient use. ANSI 16 colors
and basic style attributes only. All values are set to empty string if NO_COLOR
environment variable is set or if program is not running inside of interactive
TTY, i.e. colors are automatically disabled during redirection or piping.

Usage:

    from lib.colors import attr, fg

    print(f"{fg.bright_red}Hello, 世界{attr.reset}")

Author: Göran Gustafsson <gustafsson.g@gmail.com>
License: BSD 3-Clause
"""

# flake8: noqa: E221

import os
import sys

from dataclasses import dataclass


@dataclass(frozen=True)
class Attributes:
    """Terminal style attributes."""

    reset:     str = ""
    bold:      str = ""
    italic:    str = ""
    underline: str = ""
    blink:     str = ""
    reverse:   str = ""


@dataclass(frozen=True)
class Colors:
    """Terminal background & foreground colors."""

    black:   str = ""
    red:     str = ""
    green:   str = ""
    yellow:  str = ""
    blue:    str = ""
    magenta: str = ""
    cyan:    str = ""
    white:   str = ""

    bright_black:   str = ""
    bright_red:     str = ""
    bright_green:   str = ""
    bright_yellow:  str = ""
    bright_blue:    str = ""
    bright_magenta: str = ""
    bright_cyan:    str = ""
    bright_white:   str = ""


# Check if running inside of TTY and if NO_COLOR is not set.
if sys.stdout.isatty() and os.getenv("NO_COLOR") is None:
    attr = Attributes(
        reset     = "\033[0m",
        bold      = "\033[1m",
        italic    = "\033[3m",
        underline = "\033[4m",
        blink     = "\033[5m",
        reverse   = "\033[7m",
    )

    bg = Colors(
        black   = "\033[40m",
        red     = "\033[41m",
        green   = "\033[42m",
        yellow  = "\033[43m",
        blue    = "\033[44m",
        magenta = "\033[45m",
        cyan    = "\033[46m",
        white   = "\033[47m",

        bright_black   = "\033[100m",
        bright_red     = "\033[101m",
        bright_green   = "\033[102m",
        bright_yellow  = "\033[103m",
        bright_blue    = "\033[104m",
        bright_magenta = "\033[105m",
        bright_cyan    = "\033[106m",
        bright_white   = "\033[107m",
    )

    fg = Colors(
        black   = "\033[30m",
        red     = "\033[31m",
        green   = "\033[32m",
        yellow  = "\033[33m",
        blue    = "\033[34m",
        magenta = "\033[35m",
        cyan    = "\033[36m",
        white   = "\033[37m",

        bright_black   = "\033[90m",
        bright_red     = "\033[91m",
        bright_green   = "\033[92m",
        bright_yellow  = "\033[93m",
        bright_blue    = "\033[94m",
        bright_magenta = "\033[95m",
        bright_cyan    = "\033[96m",
        bright_white   = "\033[97m",
    )
else:
    # Use default type values, i.e. empty strings.
    attr = Attributes()
    bg = Colors()
    fg = Colors()
