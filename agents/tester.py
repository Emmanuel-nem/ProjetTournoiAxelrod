class tester:
    def __init__(self):
        self.riposte = False
        pass

    def choix(self, tour_courant : int, choix_autre_agent : str):
        if(tour_courant == 0): return "D"
        if(choix_autre_agent == "D"):
            self.riposte = True
        if(self.riposte == True): return choix("TIT-FOR-TAT", tour_courant-1, choix_autre_agent)
        else:
            if(tour_courant%3 == 0): return "D"
            else: return "C"