"""CLASS PLAYER AND ENEMY FOR GAME"""

import random
from settings import LIVES, exodus_1, exodus_2
from exeptions import GameOver, EnemyDown


class Enemy:
    def __init__(self, level: int):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack() -> int:
        return random.randint(1, 3)

    def decrease_lives(self) -> None:

        if self.lives > 0:
            self.lives -= 1
        else:
            raise EnemyDown()


class Player:

    def __init__(self, name):
        self.name = name
        self.lives = LIVES
        self.score = 0

    @staticmethod
    def fight(attack, defence) -> int:
        if attack - defence in exodus_1:
            return 1

        elif attack - defence in exodus_2:
            return -1

        else:
            return 0

    def decrease_lives(self) -> None:
        if self.lives > 0:
            print(f"You have {self.lives} lives left\n")
            self.lives -= 1

        else:
            print(f"You scored: {self.score}")
            raise GameOver

    def attack(self, enemy_obj: Enemy) -> None:
        choice_attack = int(input("Choose who you want to attack: "))
        outcome = self.fight(choice_attack, enemy_obj.select_attack())

        if outcome == 0:
            print("It's a draw\n")

        elif outcome == -1:
            print("You missed\n")

        elif outcome == 1:
            print("You attacked successfully !\n")
            enemy_obj.decrease_lives()
            self.score += 1

    def defence(self, enemy_obj: Enemy) -> None:
        choice_attack = int(input("Choose who you want to protect: "))
        outcome = self.fight(enemy_obj.select_attack(), choice_attack)

        if outcome == 0:
            print("It's a draw\n")

        elif outcome == 1:
            print("You missed\n")
            self.decrease_lives()

        elif outcome == -1:
            print("You attacked successfully !\n")
            enemy_obj.decrease_lives()
            self.score += 1


def get_player_instance() -> Player:
    user_name = check_name()
    while True:
        choice = input("Enter start for start the game: ")
        if choice == "start":
            rules()
            return Player(user_name)


def check_name():
    while True:
        user_name = input("Enter your name: ")
        if len(user_name) > 2 and user_name.isalpha():
            return user_name.capitalize()


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
