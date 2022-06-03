# 4. Scrie o clasa ce repr. o cursa aeriana
# Atr:
#  - aeroport_plecare
#  - aeroport_sosire
#  - data_ora_plecare
#  - data_ora_sosire
#  - pret_per_loc

# Meth:
#  - get_duration
#  - get_price_tva
from datetime import datetime
from air_travel import AirPlane, AirTrip, Ticket

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


d_time = datetime(2022, 6, 2, 12, 30)
a_time = datetime(2022, 6, 2, 13, 10)

trip1 = AirTrip("BUC", "TIM", d_time, a_time, 100)
airbus = AirPlane(20, 4)

ticket_list = []

for name in calatori:
    ticket_list.append(Ticket(name, airbus.get_next_free_seats(), trip1))

for i in ticket_list:
    i.print_ticket()

