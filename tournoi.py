from agents.all_d import all_d
from agents.randomagent import randomagent
from agents.tit_for_tat import tit_for_tat
from agents.tester import tester
from agents.joss import joss

class tournoi:
    def __init__(self):
        self.strategies = ["ALL-D", "RANDOM", "TIT-FOR-TAT", "TESTER", "JOSS"]

    def duel(self, strategie1,strategie2):
        match strategie1:
            case "ALL-D":
                a1 = all_d()
            case "RANDOM":
                a1 = randomagent()
            case "TIT-FOR-TAT":
                a1 = tit_for_tat()
            case "TESTER":
                a1 = tester()
            case "JOSS":
                a1 = joss()
                
        match strategie2:
            case "ALL-D":
                a2 = all_d()
            case "RANDOM":
                a2 = randomagent()
            case "TIT-FOR-TAT":
                a2 = tit_for_tat()
            case "TESTER":
                a2 = tester()
            case "JOSS":
                a2 = joss()
        
        tour = 0
        choix_a1 = None
        choix_a2 = None
        score_a1 = 0
        score_a2 = 0

        for i in range(200):
            c1 = a1.choix(tour, choix_a2)
            c2 = a2.choix(tour, choix_a1)
            tour += 1
            choix_a1 = c1
            choix_a2 = c2
            
            match choix_a1:
                case "D":
                    if(choix_a2 == "D"):
                        score_a1 += 2
                        score_a2 += 2
                    else: 
                        score_a1 += 5
                        score_a2 += 0
                case "C":
                    if(choix_a2 == "D"):
                        score_a1 += 0
                        score_a2 += 5
                    else: 
                        score_a1 += 3
                        score_a2 += 3
        return(score_a1, score_a2)
    
    def axelrod(self):
        scores = []
        s1 = 0
        s2 = 0
        for i in range(len(self.strategies)):
            scores.append(0)
        
        for strat1 in range(len(self.strategies)):
            for strat2 in range(strat1 +1,len(self.strategies)):
                if strat2 != strat1:
                    for num_match in range(5):
                        s1, s2 = self.duel(self.strategies[strat1], self.strategies[strat2])
                        scores[strat1] += s1
                        scores[strat2] += s2
        
        for i in range(len(self.strategies)):
            print("Stratégie : ", self.strategies[i], "     Score : ", scores[i])
        