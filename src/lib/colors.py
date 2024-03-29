"""Terminal colors library.

Contains functions that generate data structures with preset terminal color and
attribute string values to allow for easy use with standard print functions.
ANSI 16 colors and basic style attributes only. By default all values are set
to empty string if 'NO_COLOR' environment variable is set or if program is not
running inside of interactive TTY, i.e. colors are automatically disabled
during redirection or piping.

Function init_auto() is automatically executed for user convenience. Functions
init_on() and init_off() can be used to override with specific behaviour, e.g.
to support implementation of '--color=on/off' argument.

Structure:

    colors
    |-- attr
    |   |-- blink
    |   |-- bold
    |   |-- italic
    |   |-- reset
    |   |-- reverse
    |   `-- underline
    |-- bg
    |   |-- black
    |   |-- blue
    |   |-- cyan
    |   |-- green
    |   |-- magenta
    |   |-- red
    |   |-- white
    |   |-- yellow
    |   |-- bright_black
    |   |-- bright_blue
    |   |-- bright_cyan
    |   |-- bright_green
    |   |-- bright_magenta
    |   |-- bright_red
    |   |-- bright_white
    |   `-- bright_yellow
    `-- fg
        |-- black
        |-- blue
        |-- cyan
        |-- green
        |-- magenta
        |-- red
        |-- white
        |-- yellow
        |-- bright_black
        |-- bright_blue
        |-- bright_cyan
        |-- bright_green
        |-- bright_magenta
        |-- bright_red
        |-- bright_white
        `-- bright_yellow

Usage:

    from lib import colors

    print(f"{colors.fg.bright_red}Hello, 世界{colors.attr.reset}")

Author: Göran Gustafsson <gustafsson.g@gmail.com>
License: BSD 3-Clause
"""

# flake8: noqa: E221
# pylint: disable=global-statement

import os
import sys

from dataclasses import dataclass


@dataclass(frozen=True)
class Attributes:
    """Terminal style attributes."""

    blink:     str = ""
    bold:      str = ""
    italic:    str = ""
    reset:     str = ""
    reverse:   str = ""
    underline: str = ""


@dataclass(frozen=True)
class Colors:
    """Terminal background & foreground colors."""

    black:   str = ""
    blue:    str = ""
    cyan:    str = ""
    green:   str = ""
    magenta: str = ""
    red:     str = ""
    white:   str = ""
    yellow:  str = ""

    bright_black:   str = ""
    bright_blue:    str = ""
    bright_cyan:    str = ""
    bright_green:   str = ""
    bright_magenta: str = ""
    bright_red:     str = ""
    bright_white:   str = ""
    bright_yellow:  str = ""


# Using global variables to keep state without hassle for users.
attr, bg, fg = Attributes(), Colors(), Colors()


def init_auto():
    """Run either init_on() or init_off().

    If program is running inside of interactive TTY and 'NO_COLOR' environment
    variable is not set use function init_on(), otherwise use init_off().
    """

    if sys.stdout.isatty() and os.getenv("NO_COLOR") is None:
        init_on()
    else:
        init_off()


def init_on():
    """Set data structures with preset attribute and color values."""

    global attr, bg, fg
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


def init_off():
    """Set data structures with empty attribute and color values."""

    # Use default values, i.e. empty strings.
    global attr, bg, fg
    attr, bg, fg = Attributes(), Colors(), Colors()


# Start automatic mode by default for user convenience.
init_auto()
