from app_logic import AppLogic


class UI:
    def __init__(self):
        self._app = None

    def run(self):
        if True:
            input_file = input("Input file name: ")
            markov_degree = int(input("Markov chain degree: "))
            output_file = input("Output file name: ")
        else:
            input_file = "test_data.txt"
            markov_degree = 2
            output_file = "test_output.txt"

        self._app = AppLogic(input_file, output_file, markov_degree)
        self._app.run()
