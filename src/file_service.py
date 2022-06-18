import os


class FileService:
    """Class responsible for file handling and data preparation.
    """

    def __init__(self):
        pass

    def read_file(self, filename: str):
        """Reads data from file.

        Args:
            filename (str): Input data filename.

        Returns:
            List containing the input data.
        """
        dirname = os.path.dirname(__file__)
        data_path = os.path.join(dirname, "..", "data", "input", filename)

        output = []

        with open(data_path) as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split()
                for part in parts:
                    output.append(part)

        return output

    def create_sequences(self, data: list, sequence_length: int):
        """Creates the data sequences that can be inserted into a Trie.

        Args:
            data (list): Input data.
            sequence_length (int): Length of one sequence.

        Returns:
            List containing the data sequences.
        """
        sequences = []

        for index in range(len(data)-sequence_length+1):
            sequences.append(data[index:index+sequence_length])

        return sequences

    def write_file(self, input_data: list, filename: str):
        """Writes data into a file.

        Args:
            input_data (list): Data to be stored.
            filename (str): Name of the output file.
        """
        dirname = os.path.dirname(__file__)
        data_path = os.path.join(dirname, "..", "data", "output", filename)

        n = 4
        input_rows = [input_data[i:i+n] for i in range(0, len(input_data), n)]

        with open(data_path, "w") as file:
            for row in input_rows:
                file.write(" ".join(row) + "\n")
