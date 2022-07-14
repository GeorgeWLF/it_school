import csv
import pathlib
from tkinter import N

root = pathlib.Path(__file__).parent
files_path = root.joinpath("files")

try:
    with open(files_path.joinpath("salari.csv")) as fin:
        reader = list(csv.reader(fin))
except OSError:
    print("File error.")
else:
    salari = []
    for i in reader:
        salari.append(int(i[3]))

    print(f"Total salarii: {sum(salari)}")
        

