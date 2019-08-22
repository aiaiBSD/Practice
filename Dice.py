import random
class Dice :
    def __init__ (self, colorful = "") :
        self.sides = 6
        self.color = colorful

    def roll (self) :
        return random.randint (1, 6)

    def __str__ (self) :
        print (self.roll())

die1 = Dice('red')
die1.__str__()


class Player:
    def __init__ (self, iden = "") :
        self.chips = 12
        self.name = iden

    def getChips (self) :
        return self.chips

    def changeChips (self, change) :
        self.chips += change


class Bouncer:
    def __init__ (self)
        player1 = Player("Alan")
        player2 = Player("Mark")
        player3 = Player("Patchen")
        player4 = Player("Dante")
        player5 = Player("Scott")
        player6 = Player("Aaron")
        players = [player1, player2, player3, player4, player5, player6]


