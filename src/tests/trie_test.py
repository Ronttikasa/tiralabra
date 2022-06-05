import unittest
from trie import Trie


class TestTrieNode(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.root = self.trie._root
        self.trie.insert_sequence(["Dm", "C"])

    def test_constructor_creates_empty_root_node(self):
        empty_root = Trie()._root
        self.assertEqual(empty_root.chord, None)
        self.assertEqual(empty_root.children, {})

    def test_insert_one_sequence(self):
        self.assertEqual(len(self.root.children), 1)

    def test_grandchild_added(self):
        child = self.root.children["Dm"]
        self.assertEqual(len(child.children), 1)

    def test_insert_different_sequences(self):
        self.trie.insert_sequence(["Gm", "Bb"])
        self.assertEqual(len(self.root.children), 2)

    def test_insert_sequences_with_common_beginning(self):
        self.trie.insert_sequence(["Dm", "Gm"])
        self.assertEqual(len(self.root.children), 1)
        self.assertEqual(len(self.root.children["Dm"].children), 2)

    def test_find_next(self):
        self.trie.insert_sequence(["Dm", "Gm", "Am"])
        self.trie.insert_sequence(["Dm", "Gm", "Em"])
        self.trie.insert_sequence(["Dm", "C", "Dm"])
        children = self.trie.find_next_chords(["Dm", "Gm"])

        self.assertEqual(len(children), 2)

    def test_find_first(self):
        self.trie.insert_sequence(["Dm", "Gm", "Am"])
        self.trie.insert_sequence(["Dm", "Gm", "Em"])
        self.trie.insert_sequence(["Dm", "C", "Dm"])
        children = self.trie.find_next_chords([])

        self.assertEqual(len(children), 1)

    def test_no_matching_sequence(self):
        self.trie.insert_sequence(["Dm", "Gm", "Am"])
        self.trie.insert_sequence(["Dm", "Gm", "Em"])
        self.trie.insert_sequence(["Dm", "C", "Dm"])
        children = self.trie.find_next_chords(["Dm", "Am"])

        self.assertFalse(children)
