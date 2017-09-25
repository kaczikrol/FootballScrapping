import random as r
import matplotlib.pyplot as plt
import numpy as np

class Team:
    def __init__(self,name,city,country):
        self.name=name
        self.city=city
        self.country=country
    def getName(self):
        return self.name
    def getCity(self):
        return self.city
    def getCountry(self):
        return self.country

class Player:
    def __init__(self,name,surname,number,position):
        self.name=name
        self.surname=surname
        self.number=number
        self.position=position
        self.attack=r.randint(40,100)
        self.midfield=r.randint(40,100)
        self.defence=r.randint(40,100)
        self.grade=(self.midfield/4+self.attack/2+self.defence/3)-8
    def getName(self):
        return self.name
    def getSurname(self):
        return self.surname
    def getNumber(self):
        return self.number
    def getPosition(self):
        return self.position
    def getStatistics(self):
        return self.attack,self.midfield,self.defence
    def getGrade(self):
        return int(self.grade)


def Match(playerA,playerB):
    statisticsA=playerA.getStatistics()
    statisticsB=playerB.getStatistics()
    resultsA=0
    resultsB=0
    for i in range(len(statisticsA)):
        if statisticsA[i]>statisticsB[2-i]:
            resultsA+=r.randint(1,5)
        if statisticsA[i]==statisticsB[i]:
            resultsA+=r.randint(0,2)
            resultsB+=r.randint(0,2)
        if statisticsB[i]>statisticsA[2-i]:
            resultsB+=r.randint(1,5)
    if resultsA>5 or resultsB>5:
        resultsA=int(resultsA*abs(np.random.normal(0,1)))
        resultsB=int(resultsB*abs(np.random.normal(0,1)))

    if resultsA>resultsB:
        print("Player A wins")
    elif resultsA==resultsB:
        print("Draw")
    else:
        print("Player B wins")

    return resultsA,resultsB


def main():
    playerA=Player("Przemyslaw","Kaczmarek","9","ATT")
    playerB=Player("Adam","Jóźwina","11","MID")
    print(playerA.getName(),playerA.getSurname(),playerA.getStatistics())
    print("Skills: ",playerA.getGrade())
    print(playerB.getName(),playerB.getSurname(),playerB.getStatistics())
    print("Skills: ",playerB.getGrade())
    resultA, resultB=Match(playerA,playerB)
    print("Player A: ",resultA," Player B: ", resultB)


main()


