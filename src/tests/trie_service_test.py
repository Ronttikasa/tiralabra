import unittest
from unittest.mock import Mock
from trie_service import TrieService


class TestTrieService(unittest.TestCase):
    def setUp(self):
        self.trie = Mock()
        self.service = TrieService(self.trie)

    def test_correct_sequences_inserted(self):
        sequences = [["Dm", "F", "C"], ["Dm", "C", "Bb"], ["Gm", "Dm", "Gm"]]
        self.service.insert(sequences)

        self.assertEqual(self.trie.insert_sequence.call_count, 3)
        self.trie.insert_sequence.assert_called_with(["Gm", "Dm", "Gm"])
