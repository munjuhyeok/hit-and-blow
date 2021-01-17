import numpy as np
import itertools


class HitAndBlow:
    def __init__(self):
        self.possible_cases = set(itertools.product([1,2,3,4,5,6],repeat = 4))

    def num_hit(self,guess:tuple, answer:tuple):
        num = 0
        for g,a in zip(guess,answer):
            if (g==a):
                num +=1
        return num

    def num_blow(self,guess:tuple, answer:tuple): # hit is also considered as blow here
        num = 0
        guess = list(guess)
        answer = list(answer)
        for i in range(1,7):
            num += min(guess.count(i), answer.count(i))
        return num

    def reflect_clue(self,guess:tuple, hit:int, blow:int):
        temp = self.possible_cases.copy()
        for case in temp:
            if not (self.num_hit(guess, case) == hit and self.num_blow(guess, case) == (hit+blow)):
                self.possible_cases.remove(case)

hitandblow = HitAndBlow()
while(True):
    guess = input("your guess:")
    guess = (int(guess[0]),int(guess[1]),int(guess[2]),int(guess[3]))
    hit = int(input("hit:"))
    blow = int(input("blow:"))
    hitandblow.reflect_clue(guess,hit,blow)
    print(hitandblow.possible_cases)