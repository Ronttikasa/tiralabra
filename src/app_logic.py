from services.trie_service import TrieService
from repositories.file_service import FileService
from utilities.abcparser import ABCParser


class AppLogic:
    def __init__(self, file_svc=None, trie_svc=None, parser=None):
        self._file_svc = file_svc or FileService()
        self._trie_svc = trie_svc or TrieService()
        self._parser = parser or ABCParser()
        self._key = ""

    def _reset_key(self):
        """Reset the key signature of teaching data.
        """
        self._key = ""

    def _read_teaching_data(self, filename: str):
        """Read teaching data from input file and separates the individual tunes in the data.
        """
        success, read_data = self._file_svc.read_file(filename)

        if success:
            result = []
            tune = []
            for row in read_data:
                if row[0] == "X" and tune:
                    result.append(tune)
                    tune = []
                if not self._key and row[0] == "K":
                    self._key = row[3:]
                tune.append(row)
            result.append(tune)

            return True, result
        return False, read_data

    def _parse_abc(self, abc_data: list):
        """Convert the abc note data into a list.
        """
        result = []
        for tune in abc_data:
            result += self._parser.prep_abc_for_trie(tune)
        return result

    def _insert_into_trie(self, notes_data: list, trie_depth: int):
        """Insert parsed abc data into a Trie.
        """
        sequences = self._file_svc.create_sequences(notes_data, trie_depth)
        self._trie_svc.insert(sequences)

    def teaching_data_to_trie(self, filename: str, trie_depth: int):
        """Read teaching data file and insert it into a Trie.

        Args:
            filename (str): Teaching data file name
            trie_depth (int): Length of sequences to insert into Trie
        """
        self._reset_key()
        success, read_data = self._read_teaching_data(filename)
        if success:
            parsed_data = self._parse_abc(read_data)
            self._insert_into_trie(parsed_data, trie_depth)
            return True, None
        else:
            return False, read_data

    def _generate_tune(self, markov_degree: int, bars: int):
        """Generate a specified number of bars based on the teaching data.
        """
        tune_length = bars * 8
        generated_data = self._trie_svc.generate_sequence(
            markov_degree, tune_length
        )
        if not generated_data:
            return None
        return generated_data

    def _convert_to_abc_format(self, notes_data: list, title: str):
        return self._parser.convert_to_abc(notes_data, title, self._key)

    def _save_abc_file(self, abc_data: list, filename: str):
        self._file_svc.write_file(abc_data, filename)

    def generate_and_save(self, markov_degree: int, bars: int, title: str):
        """Generate music in abc format and write to a file.

        Args:
            markov_degree (int): Markov chain degree (lower = more randomness).
            bars (int): Number of bars to generate.
            title (str): Title of generated tune.

        Returns:
            bool
        """
        generated_tune = self._generate_tune(markov_degree, bars)
        if generated_tune:
            abc_data = self._convert_to_abc_format(generated_tune, title)
            filename = f'{title.replace(" ", "_")}_{markov_degree}.txt'
            self._save_abc_file(abc_data, filename)
            return True
        return False
