import unittest
from tools.abcparser import ABCParser


class TestABCParser(unittest.TestCase):
    def setUp(self):
        self.parser = ABCParser()
        self.data1 = [
            "X: 2",
            "T: The Maid Behind The Bar",
            "R: reel",
            "M: 4/4",
            "L: 1/8",
            "K: Dmaj",
            "|:FAAB AFED|FA(3AAA ABde|fBBA Bcde|fBBA BcdA|",
            "FAAB AFED|FAAB ABde|fBBA BcdB|AFEF D4:|"
        ]
        self.data2 = [
            "|:F,Aa'B", "FA(3AAA:|"
        ]

    def test_header_removed(self):
        abc_part = [
            "|:FAAB AFED|FA(3AAA ABde|fBBA Bcde|fBBA BcdA|",
            "FAAB AFED|FAAB ABde|fBBA BcdB|AFEF D4:|"
        ]
        output = self.parser._remove_header(self.data1)
        self.assertEqual(output, abc_part)

    def test_strip_extra_characters(self):
        cleaned_abc = ["F", "," ,"A", "a", "'", "B", "F", "A", "(", "3", "A", "A", "A"]
        output = self.parser._strip_extra(self.data2)
        self.assertEqual(output, cleaned_abc)
