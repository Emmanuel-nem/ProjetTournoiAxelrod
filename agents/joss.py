class joss:
    def __init__(self):
        pass

    def choix(self, tour_courant : int, choix_autre_agent : str):
        if(tour_courant == 0): return "C"
        elif(tour_courant % 10 == 0): return "D"
        else: return choix_autre_agent