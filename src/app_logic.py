from trie_service import TrieService
from file_service import FileService
from tools.abcparser import ABCParser


class AppLogic:
    def __init__(self, file_svc=None, trie_svc=None, parser=None):
        self._file_svc = file_svc or FileService()
        self._trie_svc = trie_svc or TrieService()
        self._parser = parser or ABCParser()
        self._key = ""

    def _reset_key(self):
        self._key = ""

    def _read_teaching_data(self, filename: str):
        input_data = self._file_svc.read_file(filename)

        result = []
        tune = []
        for row in input_data:
            if row[0] == "X" and tune:
                result.append(tune)               
                tune = []
            if not self._key and row[0] == "K":
                self._key = row[3:]
            tune.append(row)
        result.append(tune)

        return result

    def _parse_abc(self, abc_data: list):
        result = []
        for tune in abc_data:
            result += self._parser.prep_abc_for_trie(tune)
        return result

    def _insert_into_trie(self, notes_data: list, trie_depth: int):
        sequences = self._file_svc.create_sequences(notes_data, trie_depth)
        self._trie_svc.insert(sequences)

    def teaching_data_to_trie(self, filename: str, trie_depth: int):
        self._reset_key()
        read_data = self._read_teaching_data(filename)
        parsed_data = self._parse_abc(read_data)
        self._insert_into_trie(parsed_data, trie_depth)

    def _generate_tune(self, markov_degree: int, bars: int):
        tune_length = bars * 8
        generated_data = self._trie_svc.generate_sequence(
            markov_degree, tune_length
        )
        return generated_data

    def _convert_to_abc_format(self, notes_data: list, title: str):
        return self._parser.convert_to_abc(notes_data, title, self._key)

    def _save_abc_file(self, abc_data: list, filename: str):
        self._file_svc.write_file(abc_data, filename)

    def generate_and_save(self, markov_degree: int, bars: int, title: str):
        generated_tune = self._generate_tune(markov_degree, bars)
        abc_data = self._convert_to_abc_format(generated_tune, title)
        filename = f'{title.replace(" ", "_")}_{markov_degree}.txt'
        self._save_abc_file(abc_data, filename)

    # def run(self):
    #     raw_input_data = self._file_svc.read_file(self._input)
    #     input_data = self._file_svc.create_sequences(
    #         raw_input_data, self._markov_deg+1)
    #     self._trie_svc.insert(input_data)

    #     generated_output = self._trie_svc.generate_sequence(
    #         self._markov_deg, 16)
    #     self._file_svc.write_file(generated_output, self._output)
