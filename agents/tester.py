class tester:
    def __init__(self):
        self.riposte = False
        pass

    def choix(self, tour_courant : int, choix_autre_agent : str):
        if(tour_courant == 0): return "D"
        if(self.riposte == True): return choix_autre_agent
        if(choix_autre_agent == "D"):
            self.riposte = True
            return "C"
        else:
            if(tour_courant%3 == 0): return "D"
            else: return "C"