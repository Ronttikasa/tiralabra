import unittest
from unittest.mock import Mock
from trie_service import TrieService
from trie import Trie


class TestTrieService(unittest.TestCase):
    def setUp(self):
        self.trie = Mock(wraps=Trie())
        self.service = TrieService(self.trie)

        self.trie2 = Mock(wraps=Trie())
        self.service2 = TrieService()
        self.input_data = [["Dm", "C", "Bb"], ["C", "Bb", "Dm"], ["Bb", "Dm", "C"], ["Dm", "C", "Gm"],
                           ["C", "Gm", "Bb"], ["Gm", "Bb", "C"], ["Bb", "C", "Dm"], ["C", "Dm", "C"]]
        self.service2.insert(self.input_data)

    def test_insert_calls_trie_insert_function(self):
        sequences = [["Dm", "F", "C"], ["Dm", "C", "Bb"], ["Gm", "Dm", "Gm"]]
        self.service.insert(sequences)

        self.assertEqual(self.trie.insert_sequence.call_count, 3)
        self.trie.insert_sequence.assert_called_with(["Gm", "Dm", "Gm"])

    def test_sequence_inserted(self):
        self.service.insert([["Dm", "F", "C"]])
        self.assertTrue("Dm" in self.trie._root.get_children().keys())

    def test_next_chord_selection_with_one_child(self):
        node = Mock()
        node.get_occurrences.return_value = 3
        chords = {"Dm": node}

        selected_chord = self.service._select_next_chord(chords)
        self.assertEqual(selected_chord, "Dm")

    def test_next_chord_selection_with_more_children(self):
        node_1 = Mock()
        node_1.get_occurrences.return_value = 5
        node_2 = Mock()
        node_2.get_occurrences.return_value = 5
        chords = {"Dm": node_1, "C": node_2}

        for _ in range(10):
            selected_chord = self.service._select_next_chord(chords)
            self.assertTrue(selected_chord in ["Dm", "C"])

    def test_correct_length_sequence_generated(self):
        for length in range(10):
            output = self.service2.generate_sequence(2, length)
            self.assertEqual(len(output), length)

    def test_generated_sequences_are_allowed(self):
        output = self.service2.generate_sequence(2, 25)
        output_sequences = []
        for i in range(len(output)-2):
            output_sequences.append(output[i:i+3])

        for seq in output_sequences:
            self.assertTrue(seq in self.input_data)
