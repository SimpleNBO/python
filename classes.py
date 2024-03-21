class Flight():
    def __init__(self, capactity):
        self.capacity = capactity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ['Harry', 'Ron', 'Hermioni', 'Ginny']
for person in people:
    if flight.add_passenger(person):
        print(f'Added {person} to the flight of capacity {flight.capacity}')
    else:
        print(f'No available seats for {person} in flight with the capacity of {flight.capacity}')