class AirPlane:
    """Airplane class."""

    def __init__(self, rows, cols):
        """New airplane object.
        Params:
            - rows: airplane seat rows
            - cols: airplane seat cols
        """
        self.__rows = rows
        self.__cols = cols
        self.__seats = self.generate_seat_numbers()


    def get_total_seats(self):
        """Returs total number of seats"""
        return self.__rows * self.__cols

    # A B C D E F ....
    # 1
    # 2
    # 3

    def generate_seat_numbers(self):
        """Genereates seat numbers based on cols and rows.
        As following 1A, 2A, 3A....
        """
        seats = []
        for c in range(65, 65 + self.__cols):
            for r in range(1, self.__rows + 1):
                seats.append(str(r) + chr(c))

        return seats

    def get_next_free_seats(self):
        """Return next avaible seats"""
        self.__cols += 1
        if self.__cols < len(self.__seats):
            return self.__seats[self.__cols]
        else:
            return None


class AirTrip:

    def __init__(self, depart_airport, arrive_airport, depart_time, arrival_time, price):
        self.__depart_airport = depart_airport
        self.__arive_airport = arrive_airport
        self.depart_time = depart_time
        self.arrival_time = arrival_time
        self.__price = price

    def get_depart_airport(self):
        return self.__depart_airport

    def get_arrive_airport(self):
        return self.__arive_airport

    def get_price_tva(self):
        if self.__price > 0:
            return self.__price + self.__price * 19 / 100 


class Ticket:

    def __init__(self, passenger_name, seat, trip):
        self.passenger_name = passenger_name
        self.seat = seat

        # compozitie
        if isinstance(trip, AirTrip):
            self.trip = trip
        else:
            # raise error
            print("EROARE: Nu am primit un obiect de AirTrip")

    def print_ticket(self):
        print("+-----------------------+")
        print("Passenger name:", self.passenger_name)
        print("Depart:", self.trip.get_depart_airport(), "-", self.trip.depart_time)
        print("Arrival:", self.trip.get_arrive_airport(), "-", self.trip.arrival_time)
        print()
        print("Seat:", self.seat)
        print("Price (incl. TVA):", self.trip.get_price_tva())
        print("+------------------------+")

    # scriem o metoda magica
    def __str__(self):
        return f"<Ticket object for {self.passenger_name}> "
