import random

class Player():
    hp = 100

    def __init__(self, name):
        self.name = name

    def kick(self, power):
        probability = 1 / power
        hitting = True if random.randint(1,10) * probability > 1 else False

        if hitting:
            return 3 * power
        else:
            return 0