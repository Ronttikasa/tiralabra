class TrieNode:
    """Class that represents a node in a Trie tree.

    Attributes:
        chord: Chord value of the node.
    """

    def __init__(self, chord):
        """Class constructor, creates a new node.

        Args:
            chord (str): Chord value of the node.
        """
        self.chord = chord
        self.children = {}
        self.occurrences = 1

    def add_occurrence(self):
        self.occurrences += 1

    def add_child(self, chord):
        self.children[chord] = TrieNode(chord)

    def get_children(self):
        return self.children

    def get_occurrences(self):
        return self.occurrences


class Trie:
    """Class that represents a Trie data structure"""

    def __init__(self):
        """Class constructor, creates a root node with empty chord value.
        """
        self._root = TrieNode(None)

    def insert_sequence(self, sequence: list):
        current_node = self._root
        for chord in sequence:
            if chord in current_node.children:
                current_node.children[chord].add_occurrence()
            else:
                current_node.add_child(chord)
            current_node = current_node.children[chord]

    def find_next_chords(self, sequence: list):
        current_node = self._root
        for chord in sequence:
            if chord in current_node.children:
                current_node = current_node.children[chord]
            else:
                return None
        return current_node.children
