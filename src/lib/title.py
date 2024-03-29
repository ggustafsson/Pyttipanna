"""Title capitalization library.

Contains functions used for reformatting input text following English title
capitalization rules. First word, last word, new sentences, punctuated
abbreviations, brackets () {} [] <>, quotes "" '', etc is handled correctly.
Corner case proofness is very good but should NOT be expected, it is more or
less impossible to achieve correct results on all input variations.

Lowercase:

    a, an, and, as, at, but, by, en, etc, for, from,
    if, in, of, on, or, the, to, via, von, vs, with

List of lowercase words can be overridden with secondary titleize() argument.

Example:

    Input:  "tears for fears @ rule the world: the greatest hits"
    Output: "Tears for Fears @ Rule the World: The Greatest Hits"

Usage:

    from lib import title

    title.titleize("text")

    lower = ("this", "that")
    title.titleize("text", lower)

Author: Göran Gustafsson <gustafsson.g@gmail.com>
License: BSD 3-Clause
"""

import re

# XXX: Expose globally to allow for usage in test_title.py.
_lowercase = (
    "a", "an", "and", "as", "at", "but", "by", "en", "etc", "for", "from",
    "if", "in", "of", "on", "or", "the", "to", "via", "von", "vs", "with",
)
_end_sentence = (".", ",", ":", ";", "!", "?", "&", "/", "@", "+", "-")


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


def titleize(text: str, lower: tuple = _lowercase) -> str:
    """Capitalize string following English title capitalization rules.

    Arguments:
        text: str containing text to titleize.
        lower: tuple containing all words to lowercase.

    Returns:
        str containing titleized text.
    """

    words = text.split()
    last_word = len(words) - 1
    skip_next = False
    result = []

    # Regex matching "A.Z." (or longer) abbreviation patterns.
    # XXX: Using [^\W\d_] because \w matches digits and underscore.
    abbrev = re.compile(r"^([^\W\d_]{1}\.){2,}$")

    for index, word in enumerate(words):
        # Check if current iteration should be treated as new sentence.
        skip = bool(skip_next)

        # Check if next iteration should be treated as new sentence.
        skip_next = bool(word[-1] in _end_sentence)

        # Check if end of sentence or punctuated abbreviation.
        if word[-1] == "." and abbrev.match(word):
            skip_next = False

        # Check if new sentence, first word or last word first.
        if skip or index in (0, last_word):
            result.append(title(word))
        elif str.lower(word) in lower:
            result.append(word.lower())
        else:
            result.append(title(word))

    return str.join(" ", result)
