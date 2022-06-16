class ABCParser:
    def __init__(self):
        self._headers = ["X:", "T:", "C:", "M:", "K:", "R:", "L:"]
        self._notes = "C,D,E,F,G,A,B,c'd'e'f'g'a'b'"
        self._extra_characters = "(234"

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
                if char in self._notes or char in self._extra_characters:
                    output.append(char)
        return output

    def _modify_time_values(self, sequence: list):
        """Convert other time values into corresponding number of eigth notes.

        Args:
            sequence (list): _description_

        Returns:
            _type_: _description_
        """
        output = []
        i = 0
        while i < len(sequence):
            if sequence[i] == "(":
                output.append(sequence[i+2])
                output.append(sequence[i+3])
                i += 5
            elif i < len(sequence)-1 and sequence[i+1] in "234":
                time_value = int(sequence[i+1])
                for times in range(time_value):
                    output.append(sequence[i])
                i += 2
            elif i < len(sequence)-1 and sequence[i+1] in ",'":
                output.append(sequence[i] + sequence[i+1])
                i += 2
            else:
                output.append(sequence[i])
                i += 1
        return output
        
if __name__ == "__main__":

    input_data = [
        "X: 2",
        "T: The Maid Behind The Bar",
        "R: reel",
        "M: 4/4",
        "L: 1/8",
        "K: Dmaj",
        # "E|FAAB AFED|FAAB (3AAAde|fBBA Bcde|fdgf efdB|",
        # "FAAB AFED|FAAB A2de|fBBA BcdB|AFEF D3:|",
        # "e|faag fdde|fdad fdd2|efga beef|gebe gee2|",
        "f'aaf (3baf|defd e2de|fB,BA BcdB|AFEF D3:|"
    ]

    parser = ABCParser()

    header_removed = parser._remove_header(input_data)
    print("no header:")
    print(header_removed)
    cleaned_data = parser._strip_extra(header_removed)
    print(cleaned_data)
    final_data = parser._modify_time_values(cleaned_data)
    print(final_data)

    

    