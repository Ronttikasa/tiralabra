from ast import parse
import unittest
from unittest.mock import Mock, patch
from app_logic import AppLogic


class StubFileService:
    def read_file(self, filename):
        if filename == "made_up_file.txt":
            return True, ["X: 1", "T: The Maid Behind The Bar", "K: Dmaj" "|:FAAB AFED|FAAB ABde|fBBA Bcde|fBBA BcdA|", "X: 1",
                          "T: The Sally Gardens", "K: Dmaj", "|:D3F AFDF|AFBF AFEF|A2 (3FGA BcdB|AFEF DBAB|"]
        if filename == "sally.txt":
            return True, ["T: The Sally Gardens", "K: Dmaj", "|:D3F AFDF|"]
        return False, "File doesn't exist"

    def create_sequences(self, tune, depth):
        if tune[0] == "F":
            return [["F", "A", "A"], ["A", "A", "B"]]
        if tune[0] == "A":
            return [["A", "F", "E"], ["F", "E", "D"]]
        if tune[0] == "D":
            return [["D", "D", "D"], ["D", "D", "F"], ["D", "F", "A"], ["F", "A", "F"], ["A", "F", "D"], ["F", "D", "F"]]

    def write_file(self, data, filename):
        pass


class StubABCParser:
    def prep_abc_for_trie(self, abc_data):
        if "|:FAAB" in abc_data:
            return ["F", "A", "A", "B"]
        if "AFED" in abc_data:
            return ["A", "F", "E", "D"]
        if "|:D3F AFDF|" in abc_data:
            return ["D", "D", "D", "F", "A", "F", "D", "F"]
    
    def convert_to_abc(self, data, title, key):
        return ["X: 1", f"T: {title}", f"K: {key}", "adbe cfdg|]"]




class TestAppLogic(unittest.TestCase):
    def setUp(self):
        self.app = AppLogic(file_svc=StubFileService(), parser=StubABCParser(), trie_svc=Mock())

    def test_reset_key(self):
        self.app._key = "Edor"
        self.app._reset_key()
        self.assertEqual(self.app._key, "")

    def test_read_valid_data(self):
        success, result = self.app._read_teaching_data("made_up_file.txt")
        self.assertTrue(success)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], ["X: 1", "T: The Maid Behind The Bar",
                         "K: Dmaj" "|:FAAB AFED|FAAB ABde|fBBA Bcde|fBBA BcdA|"])

    def test_no_teaching_data_file(self):
        success, result = self.app._read_teaching_data("nonexistent.txt")
        self.assertFalse(success)
        self.assertEqual(result, "File doesn't exist")

    def test_parse_abc(self):
        parsed_abc = self.app._parse_abc([["X: 1", "|:FAAB"], ["X: 2", "AFED"]])
        self.assertEqual(parsed_abc, [["F", "A", "A", "B"], ["A", "F", "E", "D"]])

    def test_insert_into_trie(self):
        self.app._insert_into_trie([["F", "A", "A", "B"], ["A", "F", "E", "D"]], 3)
        self.app._trie_svc.insert.assert_called_with([["A", "F", "E"], ["F", "E", "D"]])

    def test_from_data_to_trie(self):
        success, message = self.app.teaching_data_to_trie("sally.txt", 3)
        self.assertTrue(success)

    def test_invalid_file_name(self):
        success, message = self.app.teaching_data_to_trie("nonexistent.txt", 2)
        self.assertFalse(success)

    def test_generating_tune(self):
        self.app._trie_svc.generate_sequence.return_value = ["a", "d", "b", "e", "c", "f", "d", "g"]
        result = self.app._generate_tune(3, 1)
        self.assertEqual(result, ["a", "d", "b", "e", "c", "f", "d", "g"])

    def test_no_tune_generated(self):
        self.app._trie_svc.generate_sequence.return_value = None
        result = self.app._generate_tune(3, 1)
        self.assertFalse(result)

    def test_convert_to_abc(self):
        self.app._key = "Dmin"
        data = ["a", "d", "b", "e", "c", "f", "d", "g"]
        result = self.app._convert_to_abc_format(data, "Test song")
        self.assertEqual(result[0], "X: 1")
        self.assertEqual(result[1], "T: Test song")

    def test_save_file(self):
        app = AppLogic(file_svc=Mock(), trie_svc=Mock(), parser=Mock())
        app._save_abc_file(["a", "b", "c"], "test song")
        app._file_svc.write_file.assert_called()

    def test_generate_and_save(self):
        self.app._trie_svc.generate_sequence.return_value = ["a", "d", "b", "e", "c", "f", "d", "g"]
        success = self.app.generate_and_save(3, 1, "testing")
        self.assertTrue(success)

    def test_generate_and_save_no_sequence(self):
        self.app._trie_svc.generate_sequence.return_value = None
        success = self.app.generate_and_save(3, 4, "testing more")
        self.assertFalse(success)