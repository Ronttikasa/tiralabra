from app_logic import AppLogic


class UI:
    def __init__(self):
        self._app = AppLogic()

    def ui(self):
        print("Reel Generator")
        print("")
        print("This app generates reels (a Scottish/Irish dance tune) using Markov chains.")
        print("The app uses abc notation format. Your teaching data file should be located in /data/input")
        while True:
            self._help()
            command = input("Command: ")
            if command == "q":
                break
            if command == "r":
                input_filename = input("Input filename: ")
                markov_degree = int(
                    input("Highest Markov degree you want to use: "))
                self._app.teaching_data_to_trie(
                    input_filename, markov_degree + 1)
                print("Generate a new tune")
                tune_name = input("Name your tune: ")
                bars = int(input("Number of bars to generate: "))
                while markov_degree > 0:
                    self._app.generate_and_save(markov_degree, bars, tune_name)
                    markov_degree -= 1
            else:
                print("Command not found, try again")

    def _help(self):
        print("Commands:\n\
            r: new teaching file\n\
            q: quit")
