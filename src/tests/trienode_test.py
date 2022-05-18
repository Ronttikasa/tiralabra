import unittest
from trie import TrieNode

class TestTrieNode(unittest.TestCase):
    def setUp(self):
        self.node = TrieNode("Dm")

    def test_new_node_chord_set_correctly(self):
        self.assertEqual(self.node.chord, "Dm")

    def test_new_node_has_no_children(self):
        self.assertEqual(self.node.children, {})

    def test_new_node_occurrences_set_correctly(self):
        self.assertEqual(self.node.occurrences, 1)

    def test_add_occurrences(self):
        self.node.add_occurrence()
        self.node.add_occurrence()
        self.assertEqual(self.node.occurrences, 3)

    def test_add_child(self):
        self.node.add_child("C")
        self.assertEqual(len(self.node.children), 1)

    def test_add_child_adds_new_node(self):
        self.node.add_child("C")
        self.assertEqual(self.node.children["C"].chord, "C")
