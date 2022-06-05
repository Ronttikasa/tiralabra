from trie_service import TrieService
from file_service import FileService


class AppLogic:
    def __init__(self, input_filename, output_filename, markov_degree):
        self._input = input_filename
        self._output = output_filename
        self._markov_deg = markov_degree
        self._file_svc = FileService()
        self._trie_svc = TrieService()

    def run(self):
        raw_input_data = self._file_svc.read_file(self._input)
        input_data = self._file_svc.create_sequences(raw_input_data, self._markov_deg+1)
        self._trie_svc.insert(input_data)

        generated_output = self._trie_svc.generate_sequence(
            self._markov_deg, 16)
        self._file_svc.write_file(generated_output, self._output)
