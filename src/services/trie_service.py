from random import random
from entities.trie import Trie


class TrieService:
    """Class responsible for handling data stored in a Trie.
    """

    def __init__(self, trie=None):
        self._trie = trie or Trie()

    def insert(self, sequences: list):
        """Insert a number of chord sequences in the trie.

        Args:
            sequences (list): List of chord sequences.
        """
        for seq in sequences:
            self._trie.insert_sequence(seq)

    def _select_next_chord(self, chords: dict):
        """Draws a chord from the input based on the number of occurrences.

        Args:
            chords (dict): Dictionary where values are TrieNodes.

        Returns:
            str: The value of the selected chord.
        """
        try:
            total_sum = 0
            for chord in chords:
                total_sum += chords[chord].get_occurrences()

            probability_limits = []
            limit = 0
            for chord in chords:
                probability = chords[chord].get_occurrences() / total_sum
                limit += probability
                probability_limits.append((chord, limit))

            rand = random()

            for elem in probability_limits:
                if rand < elem[1]:
                    return elem[0]

            return probability_limits[-1][0]
        except TypeError:
            return None

    def generate_sequence(self, markov_degree: int, length: int):
        """Generates a new note sequence.

        Args:
            markov_degree (int): Markov chain degree used in the generation.
            length (int): Length of the sequence to be generated

        Returns:
            list: List of generated notes.
        """
        output = []
        previous_sequence = []

        while len(output) < length:
            next_chord_candidates = self._trie.find_next_chords(
                previous_sequence)
            next_chord = self._select_next_chord(next_chord_candidates)
            if not next_chord:
                return None

            output.append(next_chord)
            previous_sequence.append(next_chord)

            if len(previous_sequence) > markov_degree:
                previous_sequence.pop(0)

        return output
