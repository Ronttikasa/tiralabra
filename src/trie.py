class TrieNode:
    def __init__(self, chord):
        self.chord = chord
        self.children = {}
        self.occurrences = 1
        self.end = False

    def add_occurrence(self):
        self.occurrences += 1

    def add_child(self, chord):
        self.children[chord] = TrieNode(chord)

    def get_children(self):
        return self.children

    def get_child_chords(self):
        return self.children.keys()

    def set_sequence_end(self):
        self.end = True

class Trie:
    def __init__(self):
        self._root = TrieNode(None)

    def insert_sequence(self, sequence):
        current_node = self._root
        for chord in sequence:
            if chord in current_node.children:
                current_node.children[chord].add_occurrence()
            else:
                current_node.add_child(chord)
            current_node = current_node.children[chord]





