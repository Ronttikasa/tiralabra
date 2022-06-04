import os

class FileService:
    def __init__(self, filename):
        self._filename = filename

    def read(self):
        dirname = os.path.dirname(__file__)
        data_path = os.path.join(dirname, "..", "data", self._filename)

        output = []

        with open(data_path) as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")
                for part in parts:
                    output.append(part)
        
        return output

    def create_sequences(self):
        data = self.read()
        sequences = []

        for index in range(len(data)-2):
            sequences.append([data[index:index+3]])

        return sequences


