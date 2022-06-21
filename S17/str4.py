from pprint import pprint
from turtle import done


text = "hello JOHN"

calatori = [
    "Otavă Bogdan",
    "Greta Mihaela Geabelea",
    "Iustin Gabriel Manciu",
    "Corina Lungu",
    "Melissa Madalina Haj Abdo",
    "Gabriel Guțui",
    "George Valeanu",
    "Andreea-Simona Telegeanu",
    "Ionuț Alin Preda",
    "Arthur Timbalariu",
    "Cristian Laurentiu Șandor",
    "Alex Raul Bonat-Mihalca",
    "Artsanyo Dennis Kachi",
    "Sergiu Mihai Predel",
    "Marian-Gabriel Tohaneanu-Iatan",
    "Irina Florentina Barbu",
    "Cordos Simona",
]

py_text = """Python is an interpreted, interactive, object-oriented programming language. It incorporates modules, exceptions, dynamic typing, very high level dynamic data types, and classes. It supports multiple programming paradigms beyond object-oriented programming, such as procedural and functional programming. Python combines remarkable power with very clear syntax. It has interfaces to many system calls and libraries, as well as to various window systems, and is extensible in C or C++. It is also usable as an extension language for applications that need a programmable interface. Finally, Python is portable: it runs on many Unix variants including Linux and macOS, and on Windows.
To find out more, start with The Python Tutorial. The Beginner's Guide to Python links to other introductory tutorials and resources for learning Python."""


idx_virgula = py_text.find(",")  # gaseste indexul sub-stringului cautat
# print(py_text[:idx_virgula])
"""
idx_virgula = -1
done = False

while not done:
    idx_virgula = py_text.find(",", idx_virgula + 1)
    if idx_virgula != -1:
        print(idx_virgula)
    else:
        done = True
"""

py_text.replace(" ", "") # inlocuire

# count

# print(py_text.count(","))

# split, rupe in buati dupa un anumit delimitator

propozitii = py_text.split(".")

# print(propozitii)


words = py_text.split()

# pprint(words)

clean_words = []
for word in words:
    clean_words.append(word.lower().strip(",.'[]{}():;+-=<>"))

# pprint(clean_words)

# lungimea maxima a celui mai lung cuvant
max_len = 0

for word in clean_words:
    if len(word) > max_len:
        max_len = len(word)

passed_words = []
for word in clean_words:
    if word not in passed_words:
        print(word.ljust(max_len +10, "."), clean_words.count(word))
        passed_words.append(word)

name = "Alin"
surname = "Preda"

name.rjust(10) # spatii inaintea cuvantului
surname.ljust(10) # spatii dupa cuvant

# print(name.ljust(10, "_"))

name.zfill(10) # adauga 0 inaintea cuvantului

