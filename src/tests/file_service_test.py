import unittest
import os
from repositories.file_service import FileService

TESTDATA = os.path.join()


class TestTrieNode(unittest.TestCase):
    def setUp(self):
        self.trie = FileService()
        self.data_1 = [1, 2, 3, 4, 5]

    def test_created_sequences_correct_length(self):
        sequences = self.trie.create_sequences(self.data_1, 1)
        for seq in sequences:
            self.assertEqual(len(seq), 1)

        sequences = self.trie.create_sequences(self.data_1, 3)
        for seq in sequences:
            self.assertEqual(len(seq), 3)

        sequences = self.trie.create_sequences(self.data_1, 5)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(len(sequences[0]), 5)

    def test_correct_sequences_created(self):
        sequences = self.trie.create_sequences(self.data_1, 3)
        expected = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        self.assertEqual(sequences, expected)
