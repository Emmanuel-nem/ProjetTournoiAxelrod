class tit_for_tat:
    def __init__(self):
        pass

    def choix(self, tour_courant : int, choix_autre_agent : str):
        if(tour_courant == 0): return "C"
        else: return choix_autre_agent