class Pokemon:
    def __init__(self, attack, speed, hp):
        self.attack = attack
        self.speed = speed
        self.hp = hp

    def speak(self):
        print("How did this get here this code shouldn't be running")

class Charmander(Pokemon):
    def speak(self):
        print("Charmander!!")


class Squirtle(Pokemon):
    def speak(self):
        print("Squirtle!!")


def attack(p1, p2):
    pass

def battle(p1, p2):
    """
    The specifics of this function don't matter - they'd be way more complex
    if we were actually trying to code up a Pokemon game.

    (In fact, a PokemonBattle would probably be a class of its own).

    The point is that p1 and p2 could be ANY Pokemon, and the fact that
    they implement the same interface (i.e. have a common base class)
    is what lets us do this.
    """
    p1.speak()
    p2.speak()
    while (p1.hp > 0 and p2.hp > 0):
        if p1.speed >= p2.speed:
            attack(p1, p2)
            attack(p2, p1)
        else:
            attack(p2, p1)
            attack(p1, p2)


    if p1.hp > 0:
        print("P1 is the winner!")
    elif p2.hp > 0:
        print("P2 is the winner!")
    else:
        print("It's a bloodbath")



