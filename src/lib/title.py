"""Title capitalization module.

Contains functions used for reformatting input text following English title
capitalization rules. First word, last word, new sentence, brackets () {} []
<>, quotes "" '', etc is handled correctly. Corner case proofness is good but
should not be expected.

Lowercase:

    a, an, and, as, at, but, by, en, etc, for, from,
    if, in, of, on, or, the, to, via, von, vs, with

Example:

    Input:  "tears for fears @ rule the world: the greatest hits"
    Output: "Tears for Fears @ Rule the World: The Greatest Hits"

Usage:

    from lib import title

    title.titleize(string)

Author: Göran Gustafsson <gustafsson.g@gmail.com>
License: BSD 3-Clause
"""

import re

_lowercase = (
    "a", "an", "and", "as", "at", "but", "by", "en", "etc", "for", "from",
    "if", "in", "of", "on", "or", "the", "to", "via", "von", "vs", "with"
)
_end_sentence = (".", ",", ":", ";", "!", "?", "&", "/", "+", "-")


def title(text: str) -> str:
    """Capitalize every word (including sub-words) in string.

    Same as builtin str.title() but it actually works.
    See: https://docs.python.org/3/library/stdtypes.html#str.title

    Arguments:
        text: str containing text to titlecase.

    Returns:
        str containing titlecased text.
    """

    return re.sub(
        r"\w+('\w+)?",
        lambda match: match.group(0).capitalize(),
        text
    )


def titleize(text: str) -> str:
    """Capitalize string following English title capitalization rules.

    Arguments:
        text: str containing text to titleize.

    Returns:
        str containing titleized text.
    """

    words = text.split()
    last_word = len(words) - 1
    skip_next = False
    result = []

    for index, word in enumerate(words):
        # Check if current iteration should be treated as new sentence.
        skip = bool(skip_next)

        # Check if next iteration should be treated as new sentence.
        skip_next = bool(word[-1] in _end_sentence)

        # 1. Titlecase first and last word.
        # 2. Lowercase word unless new sentence.
        # 3. Titlecase everything else.
        if index in (0, last_word):
            result.append(title(word))
        elif not skip and str.lower(word) in _lowercase:
            result.append(word.lower())
        else:
            result.append(title(word))

    return str.join(" ", result)
