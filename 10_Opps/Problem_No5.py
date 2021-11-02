class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The Name of RailWay is {self.name}")
        print(f"The Seats in RailWay is {self.seats}")

    def fareInfo(self):
        print(f"The Fare of Railway is {self.fare}")

    def BookTicket(self):
        if(self.seats>0):
            print(f"Your Seat is Booked, Number is {self.seats}")
            self.seats = self.seats - 1
        else :
            print("Soory The Seats is Not Available")

    def CancelTicket(self):
        
s = Train("InterCity Express", 60, 300)
s.getStatus()
s.fareInfo()
s.BookTicket()
