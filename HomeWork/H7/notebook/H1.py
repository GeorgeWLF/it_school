# 1. Scrie o clasa care repr. o Agenda (Notebook).
# Atribute:
#     - nr pagini
#     - culoare
#     - continut - lista de stringuri ["continut pagina", "continut pag."]

# Metode:
#     - scrie in Agenda
#     - vezi nr de pag goale
#     - vezi nr pag scrise


class Notebook:
    def __init__(self, nr_of_pages, color):
        self.nr_of_pages = nr_of_pages
        self.color = color
        self.content = []

    def write_to_notebook(self, content):
        is self.empty_pages() != 0