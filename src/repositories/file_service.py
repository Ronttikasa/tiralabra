import os
from config import INPUT_DATA_DIRECTORY, OUTPUT_DATA_DIRECTORY


class FileService:
    """Class responsible for file handling and data preparation.
    """

    def __init__(self):
        pass

    def read_file(self, filename: str):
        """Read data from file.

        Args:
            filename (str): Input data filename.

        Returns:
            List containing the input data.
        """
        try:
            data_path = os.path.join(INPUT_DATA_DIRECTORY, filename)

            output = []

            with open(data_path, "r", encoding="utf-8") as file:
                for row in file:
                    row = row.replace("\n", "")
                    if row:
                        output.append(row)
            return True, output
        except FileNotFoundError:
            return False, "File doesn't exist"

    def create_sequences(self, data: list, sequence_length: int):
        """Create the data sequences that can be inserted into a Trie.

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
        """Write data into a file.

        Args:
            input_data (list): Data to be stored.
            filename (str): Name of the output file.
        """

        data_path = os.path.join(OUTPUT_DATA_DIRECTORY, filename)

        with open(data_path, "w", encoding="utf-8") as file:
            for row in input_data:
                file.write(row + "\n")
