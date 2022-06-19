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
            "|:F,Aa'B", "FA(3AAAQ:|"
        ]

        self.data3 = [
            "X: 2",
            "T: The Maid Behind The Bar",
            "R: reel",
            "M: 4/4",
            "L: 1/8",
            "K: Dmaj",
            "FAAB"
        ]

    def test_header_removed(self):
        abc_part = [
            "|:FAAB AFED|FA(3AAA ABde|fBBA Bcde|fBBA BcdA|",
            "FAAB AFED|FAAB ABde|fBBA BcdB|AFEF D4:|"
        ]
        output = self.parser._remove_header(self.data1)
        self.assertEqual(output, abc_part)

    def test_strip_extra_characters(self):
        cleaned_abc = list("F,Aa'BFA(3AAA")
        output = self.parser._strip_extra(self.data2)
        self.assertEqual(output, cleaned_abc)

    def test_triplets_handled_correctly(self):
        abc_data = list("(3aaa")
        result = self.parser._modify_time_values(abc_data)
        expected_result = list("aaa")
        self.assertEqual(result, expected_result)

    def test_number_valueshandled_correctly(self):
        abc_data = list("A4f3g2")
        expected_result = list("AAAAfffgg")
        result = self.parser._modify_time_values(abc_data)
        self.assertEqual(result, expected_result)

    def test_octaves_handled_correctly(self):
        abc_data = list("Gg'B,e")
        expected_result = ["G", "g'", "B,", "e"]
        result = self.parser._modify_time_values(abc_data)
        self.assertEqual(result, expected_result)

    def test_number_values_with_octaves_handled_correctly(self):
        abc_data = list("A,4Cf'3g2")
        expected_result = ["A,", "A,", "A,",
                           "A,", "C", "f'", "f'", "f'", "g", "g"]
        result = self.parser._modify_time_values(abc_data)
        self.assertEqual(result, expected_result)

    def test_abc_for_trie(self):
        result = self.parser.prep_abc_for_trie(self.data3)
        expected_result = list("FAAB")
        self.assertEqual(result, expected_result)

    def test_add_barlines(self):
        abc_data = ["A,", "A,", "A,", "A,", "C", "f'", "f'", "f'", "g", "g"]
        result = self.parser._add_barlines(abc_data)
        expected_result = "A,A,A,A, Cf'f'f'|gg|]"
        self.assertEqual(result, expected_result)

    def test_create_header(self):
        result1 = self.parser._generate_header("Test tune", "Dmaj")
        result2 = self.parser._generate_header("Tira tune", "Gmin")

        expected_result1 = [
            "X: 1",
            "T: Test tune",
            "M: 4/4",
            "L: 1/8",
            "K: Dmaj"
        ]
        expected_result2 = [
            "X: 1",
            "T: Tira tune",
            "M: 4/4",
            "L: 1/8",
            "K: Gmin"
        ]
        self.assertEqual(result1, expected_result1)
        self.assertEqual(result2, expected_result2)

    def test_abc_conversion(self):
        abc_data = ["A,", "A,", "A", "B", "C", "f'", "g'", "g", "e"]
        result = self.parser.convert_to_abc(abc_data, "Tira reel", "Edor")
        expected_result = [
            "X: 1",
            "T: Tira reel",
            "M: 4/4",
            "L: 1/8",
            "K: Edor",
            "A,A,AB Cf'g'g|e|]"
        ]
        self.assertEqual(result, expected_result)
