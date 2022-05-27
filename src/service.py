from trie import Trie, TrieNode

class Service:
    """Class responsible for application logic.
    """
    def __init__(self):
        self._trie = Trie()

    def insert(self, sequences: list):
        """Insert a number of chord sequences in the trie.

        Args:
            sequences (list): List of chord sequences.
        """
        for seq in sequences:
            self._trie.insert_sequence(seq)

    