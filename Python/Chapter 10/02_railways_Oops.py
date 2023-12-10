class RailwaysForm:
    formtype = "RailwaysForm"
    def printData(self):
        print(f"Name of passanger {self.name}")
        print(f"Train of passanger {self.train}")
        print(f"Time of leaving of passanger {self.timing}")
        print(f"Place of leaving of passanger {self.placeofleaving}")
        print(f"Destination of passanger {self.destination}")
        
ShadowApplication = RailwaysForm()
ShadowApplication.name = ("\u0332".join("Shadow"))
ShadowApplication.train = ("\u0332".join("Rajdhani Express"))
ShadowApplication.timing = ("\u0332".join("Monday 4:35:46 pm"))
ShadowApplication.placeofleaving = ("\u0332".join("Delhi"))
ShadowApplication.destination = ("\u0332".join("Mumbai"))
ShadowApplication.printData()