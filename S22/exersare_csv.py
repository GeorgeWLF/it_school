import csv
import pathlib

root = pathlib.Path(__file__).parent
files_path = root.joinpath("files")

# citire fisier csv
try:
    with open(files_path.joinpath("salari.csv")) as fin:
        reader = list(csv.reader(fin))
except OSError:
    print("File error.")
else:
    for i in reader:
        pass

# citire fisier csv cu nume campuri
# field_names = [
#     "first_name",
#     "last_name",
#     "id",
#     "gros_salary",
#     "days_off"
# ]
# try:
#     with open(files_path.joinpath("salarii.csv")) as fin:
#         # list -> extrage datele din generator
#         dict_reader = list(csv.DictReader(fin, fieldnames=field_names))
#         for i in dict_reader:
#             print(i)
# except OSError:
#     print("File error.")


# scriere csv
try:
    with open(files_path.joinpath("tichete_masa.csv"), "w") as fout:
        csv_writer = csv.writer(fout, lineterminator="\n")
        for i in reader:
            worked_days = 20 - int(i[4])
            food_tickets = worked_days * 20 
            csv_writer.writerow([i[0], i[1], food_tickets, worked_days])
except OSError:
    print("File write error.")

# csv.DictWriter - get a dict for each line