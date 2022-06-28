import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

data_folder = os.getenv("DEFAULT_DATA_DIRECTORY")

INPUT_DATA_DIRECTORY = os.path.join(dirname, data_folder, "input")
OUTPUT_DATA_DIRECTORY = os.path.join(dirname, data_folder, "output")
