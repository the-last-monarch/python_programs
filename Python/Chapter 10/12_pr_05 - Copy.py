class train:   
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        
    def trainInfo(self):
        print("************")
        print(f"Name of the train is {self.name}")
        
    def seatInfo(self):
        print(f"Seats available in the train are {self.seats}")
        print("************")
        
    def fareInfo(self):
        print(f"price of the ticket of the train is : Rs.{self.fare}")
          
    def bookTickets(self):
        if(self.seats>0):
            print(f"We booked your seat and your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is fully booked. Kindly try in tatkal!")
            
    # def cancelTicket(self, seatno):
    #     self.seatno = seatno
    #     if (self.seats<0):
    #         print(f"your seat number is{self.seats}")
    #     else:
    #         print("No seat left for you")
        
Rail = train("Rajdhani Express", 110, 4)
Rail.trainInfo()
Rail.seatInfo()
Rail.bookTickets()
Rail.bookTickets()
Rail.bookTickets()
Rail.trainInfo()
# Rail.cancelTicket(Rail.seatno)