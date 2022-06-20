class ABCParser:
    def __init__(self):
        self._headers = ["X:", "T:", "C:", "M:", "K:", "R:", "L:"]
        self._notes = "CDEFGABcdefgab,'(234"

    def _remove_header(self, abc_data: list):
        """Remove the abd-file header data.

        Args:
            data (list): _description_

        Returns:
            _type_: _description_
        """
        output = []
        for row in abc_data:
            if row[0:2] in self._headers:
                pass
            else:
                output.append(row)
        return output

    def _strip_extra(self, sequence: list):
        """Strip non-note characters from the abc notation.

        Args:
            sequence (list): _description_

        Returns:
            _type_: _description_
        """
        output = []
        for row in sequence:
            for char in row:
                if char in self._notes:
                    output.append(char)
        return output

    def _modify_time_values(self, sequence: list):
        """Convert other time values into corresponding number of eigth notes.

        Args:
            sequence (list): Abc notation as a list where each character is a separate element.

        Returns:
            list: Abc notation where every note value is a separate element.
        """
        output = []
        i = 0
        while i < len(sequence):
            if sequence[i] == "(":
                i += 2
            elif i < len(sequence)-1 and sequence[i+1] in "234":
                time_value = int(sequence[i+1])
                for _ in range(time_value):
                    output.append(sequence[i])
                i += 2
            elif i < len(sequence)-2 and sequence[i+1] in ",'" and sequence[i+2] in "234":
                time_value = int(sequence[i+2])
                for _ in range(time_value):
                    output.append(sequence[i] + sequence[i+1])
                i += 3
            elif i < len(sequence)-1 and sequence[i+1] in ",'":
                output.append(sequence[i] + sequence[i+1])
                i += 2
            else:
                output.append(sequence[i])
                i += 1
        return output

    def prep_abc_for_trie(self, abc_data: list):
        data_v1 = self._remove_header(abc_data)
        data_v2 = self._strip_extra(data_v1)
        data_v3 = self._modify_time_values(data_v2)
        return data_v3

    def _add_barlines(self, abc_data: list):
        output = ""
        i = 0
        while i < len(abc_data):
            output += abc_data[i]
            i += 1
            if i % 8 == 0:
                output += "|"
            elif i % 4 == 0:
                output += " "
        return output + "]"

    def _generate_header(self, title: str, key: str):
        header = ["X: 1",
            "T: " + title ,
            "M: 4/4",
            "L: 1/8",
            "K: " + key
        ]
        return header

    def convert_to_abc(self, notes_data: list, title: str, key: str):
        header = self._generate_header(title, key)
        abc_part = self._add_barlines(notes_data)
        header.append(abc_part)
        return header
