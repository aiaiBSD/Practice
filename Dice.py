import random
class Dice :
    def __init__ (self, colorful = "") :
        self.sides = 6
        self.color = colorful

    def roll (self) :
        return random.randint (1, 6)

    def __str__ (self) :
        print (self.roll())



class Player:
    def __init__ (self, iden = "") :
        self.chips = 12
        self.name = iden
        self.roll = 0

    def getChips (self) :
        return self.chips

    def getRoll (self) :
        return self.roll

    def getName (self) :
        return self.name

    def changeChips (self, change) :
        self.chips += change

    def changeRoll (self, change) :
        self.roll = change

class Bouncer:
    def __init__ (self) :
        print ('Welcome to Bouncer!')
        self.player1 = Player("Alan")
        self.player2 = Player("Mark")
        self.player3 = Player("Patchen")
        self.player4 = Player("Dante")
        self.player5 = Player("Scott")
        self.player6 = Player("Aaron")
        self.players = [self.player1, self.player2, self.player3, self.player4, self.player5, self.player6]

    def play (self) :
        self.die = Dice('white')
        self.gameEnd = True
        self.i = 1
        self.player1.changeRoll(self.die.roll())
        print ('Alan rolled ' + str(self.player1.getRoll()))
        while self.gameEnd :
            self.players[self.i].changeRoll(self.die.roll())
            print (str(self.players[self.i].getName()) + ' rolled a ' + str(self.players[self.i].getRoll()))
            if self.i == 0 :
                self.players[5].changeChips(self.players[5].getRoll() - self.players[0].getRoll())
                self.players[0].changeChips(self.players[0].getRoll() - self.players[5].getRoll())
                print ('Aaron has a chip value of ' + str(self.players[5].getChips()) + ' and Alan has a chip value of ' + str(self.players[0].getChips()))
                
            else :
                self.players[self.i - 1].changeChips(self.players[self.i - 1].getRoll() - self.players[self.i].getRoll())
                self.players[self.i].changeChips(self.players[self.i].getRoll() - self.players[self.i - 1].getRoll())
                print (str(self.players[self.i - 1].getName()) + ' has a chip value of ' + str(self.players[self.i - 1].getChips()) + ' and ' + str(self.players[self.i].getName()) + ' has a chip value of ' + str(self.players[self.i].getChips()))

            if self.players[self.i].getChips() < 0 :
                self.gameEnd = False
            elif self.players[self.i - 1].getChips() < 0 :
                self.gameEnd = False

            if self.i == 5 :
                self.i = 0
            else :
                self.i += 1
            
game = Bouncer()
game.play()
    
