"""Terminal colors module.

Contains preset terminal color and attribute values for convenient use. ANSI 16
colors and basic style attributes only. All values are set to empty string when
program is not running inside of interactive TTY, i.e. colors are disabled
during redirection or piping.

Usage:

    from lib.colors import Attr, Fg

    print(f"{Fg.BrightRed}Hello, 世界{Attr.Reset}")

Author: Göran Gustafsson <gustafsson.g@gmail.com>
License: BSD 3-Clause
"""

# flake8: noqa: E221

import sys

from dataclasses import dataclass


@dataclass(frozen=True)
class Attr:
    """Terminal style attributes."""

    if sys.stdout.isatty():
        Reset     = "\033[0m"
        Bold      = "\033[1m"
        Italic    = "\033[3m"
        Underline = "\033[4m"
        Blink     = "\033[5m"
        Reverse   = "\033[7m"
    else:
        Reset     = ""
        Bold      = ""
        Italic    = ""
        Underline = ""
        Blink     = ""
        Reverse   = ""


@dataclass(frozen=True)
class Bg:
    """Terminal background colors."""

    if sys.stdout.isatty():
        Black   = "\033[40m"
        Red     = "\033[41m"
        Green   = "\033[42m"
        Yellow  = "\033[43m"
        Blue    = "\033[44m"
        Magenta = "\033[45m"
        Cyan    = "\033[46m"
        White   = "\033[47m"

        BrightBlack   = "\033[100m"
        BrightRed     = "\033[101m"
        BrightGreen   = "\033[102m"
        BrightYellow  = "\033[103m"
        BrightBlue    = "\033[104m"
        BrightMagenta = "\033[105m"
        BrightCyan    = "\033[106m"
        BrightWhite   = "\033[107m"
    else:
        Black   = ""
        Red     = ""
        Green   = ""
        Yellow  = ""
        Blue    = ""
        Magenta = ""
        Cyan    = ""
        White   = ""

        BrightBlack   = ""
        BrightRed     = ""
        BrightGreen   = ""
        BrightYellow  = ""
        BrightBlue    = ""
        BrightMagenta = ""
        BrightCyan    = ""
        BrightWhite   = ""


@dataclass(frozen=True)
class Fg:
    """Terminal foreground colors."""

    if sys.stdout.isatty():
        Black   = "\033[30m"
        Red     = "\033[31m"
        Green   = "\033[32m"
        Yellow  = "\033[33m"
        Blue    = "\033[34m"
        Magenta = "\033[35m"
        Cyan    = "\033[36m"
        White   = "\033[37m"

        BrightBlack   = "\033[90m"
        BrightRed     = "\033[91m"
        BrightGreen   = "\033[92m"
        BrightYellow  = "\033[93m"
        BrightBlue    = "\033[94m"
        BrightMagenta = "\033[95m"
        BrightCyan    = "\033[96m"
        BrightWhite   = "\033[97m"
    else:
        Black   = ""
        Red     = ""
        Green   = ""
        Yellow  = ""
        Blue    = ""
        Magenta = ""
        Cyan    = ""
        White   = ""

        BrightBlack   = ""
        BrightRed     = ""
        BrightGreen   = ""
        BrightYellow  = ""
        BrightBlue    = ""
        BrightMagenta = ""
        BrightCyan    = ""
        BrightWhite   = ""
