import unittest
from repositories.file_service import FileService


class TestTrieNode(unittest.TestCase):
    def setUp(self):
        self.file_service = FileService()
        self.data_1 = [1, 2, 3, 4, 5]
        self.input_filename = "test_input_1.txt"

    def test_created_sequences_correct_length(self):
        sequences = self.file_service.create_sequences(self.data_1, 1)
        for seq in sequences:
            self.assertEqual(len(seq), 1)

        sequences = self.file_service.create_sequences(self.data_1, 3)
        for seq in sequences:
            self.assertEqual(len(seq), 3)

        sequences = self.file_service.create_sequences(self.data_1, 5)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(len(sequences[0]), 5)

    def test_correct_sequences_created(self):
        sequences = self.file_service.create_sequences(self.data_1, 3)
        expected = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        self.assertEqual(sequences, expected)

    def test_reading_file(self):
        result = self.file_service.read_file(self.input_filename)
        expected = ["X: 1", "T: The Maid Behind The Bar",
                    "|:FAAB AFED|FAAB ABde|fBBA Bcde|fBBA BcdA|"]
        self.assertEqual(result[1], expected)

    def test_reading_method_invalid_filename(self):
        result = self.file_service.read_file("nonexistent_file.txt")
        self.assertFalse(result[0])
