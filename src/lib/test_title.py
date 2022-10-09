#!/usr/bin/env python3
# pylint: disable=protected-access

import unittest

import title


class TestTitle(unittest.TestCase):
    def test_title(self):
        """Validate title.title() results."""

        # Test if endings with "'s" and chars "åäö" are handled correctly.
        string = "göran's top secret quote & å ä ö test..."
        expect = "Göran's Top Secret Quote & Å Ä Ö Test..."
        #          ^^  ^^                    ^ ^ ^
        self.assertEqual(title.title(string), expect)

    def test_titleize(self):
        """Validate title.titleize() results."""

        # Test if first and last word gets titlecased.
        string = "the the the"
        expect = "The the The"
        self.assertEqual(title.titleize(string), expect)

        # Test if all words in _lowercase list gets lowered.
        lower = str.join(" ", title._lowercase)
        string = f"FIRST {str.upper(lower)} LAST"
        expect = f"First {lower} Last"
        self.assertEqual(title.titleize(string), expect)

        # Test if all chars in _end_sentence list triggers new sentence.
        for char in title._end_sentence:
            string = f"first {char} the last"
            expect = f"First {char} The Last"
            self.assertEqual(title.titleize(string), expect)

        # Test if _lowercase list is ignored following bracket or quote.
        sidestep_chars = ("(", "{", "[", "<", '"', "'")
        for char in sidestep_chars:
            string = f"first {char}the last"
            expect = f"First {char}The Last"
            self.assertEqual(title.titleize(string), expect)

        # Song/album test 1.
        string = "anna von hausswolff - the truth, the glow, the fall"
        expect = "Anna von Hausswolff - The Truth, The Glow, The Fall"
        #              ^^^            ^^^^^      ^^^^^     ^^^^^
        self.assertEqual(title.titleize(string), expect)

        # Song/album test 2.
        string = "bob marley & the wailers - no woman, no cry (live)"
        expect = "Bob Marley & The Wailers - No Woman, No Cry (Live)"
        #                    ^^^^^                            ^^^^^
        self.assertEqual(title.titleize(string), expect)

        # Song/album test 3.
        string = "danzig - satan (from satan's sadists)"
        expect = "Danzig - Satan (From Satan's Sadists)"
        #                        ^^^^^      ^^
        self.assertEqual(title.titleize(string), expect)

        # Song/album test 4.
        string = "tears for fears @ rule the world: the greatest hits"
        expect = "Tears for Fears @ Rule the World: The Greatest Hits"
        #               ^^^              ^^^      ^^^^^
        self.assertEqual(title.titleize(string), expect)

        # Song/album test 5.
        string = "sepultura - r.i.p. (rest in pain)"
        expect = "Sepultura - R.I.P. (Rest in Pain)"
        #                       ^^^        ^^
        self.assertEqual(title.titleize(string), expect)


if __name__ == "__main__":
    unittest.main()
