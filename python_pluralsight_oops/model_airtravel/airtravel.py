""" Model for aircraft flights """

class Flight:
    def __init__(self,number,aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No Airline Code in '{number}'")
        if not number[:2].isupper():
            raise ValueError(f"Invalid Airline code '{number}'")
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid Route Number '{number}'")

        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan() #tuple unpacking
        self._seating = [None]+[{letter:None for letter in seats} for _ in rows]

    def number(self):           # Flight Number ex: 'HY1234'
        return self._number

    def airline(self):          # airline ex: 'HY'
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def allocate_seat(self,seat,passenger):

        row, letter = self._parse_seat(seat) # This calls the Method of Implementation Details

        if self._seating[row][letter] is not None:
            raise ValueError(f"seat {seat} occupied already")

        self._seating[row][letter] = passenger

    def _parse_seat(self, seat):        # Method of Implementation Details
        rows, seating_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seating_letters:
            raise ValueError(f"Invalid seat letter {letter}")

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat row {row_text}")

        if row not in rows:
            raise ValueError(f"Invalid row number {row}")

        return row, letter

    def relocate_passenger(self,from_seat,to_seat):
        """Relocate a passenger to different seat.

        Args:
            from_seat: The existing seat designator for the
                        passenger to be moved

            to_seat:    The new seat designator

        Returns:

        """
        from_row,from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passenger to relocate in seat {from_seat}")

        to_row,to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"seat {to_seat} occupied already")

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def making_boarding_cards(self,card_printer):
        for passenger,seat in sorted(self._passenger_seats()):          # This calls the Method of Implementation Details
            card_printer(passenger,seat,self.number(),self.aircraft_model())

    def _passenger_seats(self):             # Method of Implemtation Details
        row_numbers,seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield(passenger,f"{row}{letter}")


'''
class Aircraft:
    def __init__(self,registration,model,num_rows,num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows+1),"ABCDEFGHJ"[:self._num_seats_per_row])
'''
class Aircraft:

    def __init__(self,registration):
        self._registration = registration
    def registraion(self):
        return self._registration
    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)

class AirbusA319(Aircraft):

    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1,23), "ABCDEF"

class Boeing777(Aircraft):

    def model(self):
        return "Boeing777"

    def seating_plan(self):
        return range(1,56), "ABCDEFGHJK"


# below are the module level functions

def console_card_printer(passenger,seat,flight_number,aircraft): # module level function
    # This console_card_printer' doesnt know anything about flights and aircrafts
    # It is very loosely coupled
    output = f"| Name: {passenger}"       \
             f"  Flight: {flight_number}" \
             f"  seat: {seat}"            \
             f"  Aircraft: {aircraft}"    \
             " |"
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + "-" * (len(output) - 2) + "|"
    lines = [banner,border,output,border,banner]
    card = "\n".join(lines)
    print(card)
    print()

def make_flights():      # module level function
    #f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows=23, num_seats_per_row=6))
    f = Flight("BA758", AirbusA319("G-EUPT"))       # Duck Typing
    f.allocate_seat("12A","Guido Van Rossum")
    f.allocate_seat("15F", "Bjarne Stroustrup")
    f.allocate_seat("15E", "Anders Helgsberg")
    f.allocate_seat("1C", "John McCarthy")
    f.allocate_seat("1D", "Rich Kickey")

    g = Flight("AF72", Boeing777("F-GSPS"))         # Duck Typing
    g.allocate_seat("55K", "Larry Wall")
    g.allocate_seat("33G", "Yukihiro Mutsumoto")
    g.allocate_seat("15E", "Anders Helgsberg")
    g.allocate_seat("4B", "Brain Kernighan")
    g.allocate_seat("4A", "Dennis Ritchie")

    return f,g






