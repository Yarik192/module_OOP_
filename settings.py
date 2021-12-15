"""ALL CONSTANTS FOR GAME"""


def rules():
    print("""
    +------------------------------------------------+
    |                 RULES OF THE GAME              |
    | To win, you need to guess which card the       |
    | opponent will choose and choose the one that   |
    | will defeat the opponent's card.               |
    | Available cards: Warrior, Robber, Wizard.      |
    |        The Wizard defeats the Warrior.         |
    |        The Warrior defeats the Robber.         |
    |        The Robber defeats the Wizard.          |
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    |                 Key 1 - Warrior                |
    |                 Key 2 - Robber                 |
    |                 Key 3 - Wizard                 |
    +------------------------------------------------+""")


LIVES = 5

WARRIOR = 1
ROBBER = 2
WIZARD = 3

exodus_1 = {WARRIOR - ROBBER, ROBBER - WIZARD, WIZARD - WARRIOR}
exodus_2 = {WARRIOR - WIZARD, ROBBER - WARRIOR, WIZARD - ROBBER}
