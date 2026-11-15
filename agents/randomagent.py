import random
class randomagent:
    def __init__(self):
        pass

    def choix(self, tour_courant : int, choix_autre_agent : str):
        random.seed(9122003)
        rand = random.randint(0,1)
        if(rand == 0): return "D"
        else: return "C"