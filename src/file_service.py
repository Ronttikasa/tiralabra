import os

class FileService:
    def __init__(self):
        pass

    def read_file(self, filename: str):
        dirname = os.path.dirname(__file__)
        data_path = os.path.join(dirname, "..", "data", "input", filename)

        output = []

        with open(data_path) as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")
                for part in parts:
                    output.append(part)
        
        return output

    def create_sequences(self, filename: str):
        data = self.read_file(filename)
        sequences = []

        for index in range(len(data)-2):
            sequences.append([data[index:index+3]])

        return sequences

    def write_file(self, input: list, filename: str):
        dirname = os.path.dirname(__file__)
        data_path = os.path.join(dirname, "..", "data", "output", filename)
        
        n = 4
        input_rows = [input[i:i+n] for i in range(0, len(input), n)]

        with open(data_path, "w") as file:
            for row in input_rows:
                file.write(" ".join(row) + "\n")


