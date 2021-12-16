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
        self.lives -= 1
        if self.lives < 1:
            pass
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

        if outcome == 1:
            print("You attacked successfully !\n")
            enemy_obj.decrease_lives()
            self.score += 1

        elif outcome == -1:
            print("You missed\n")

        else:
            print("It's a draw\n")

    def defence(self, enemy_obj: Enemy) -> None:
        choice_attack = int(input("Choose who you want to protect: "))
        outcome = self.fight(enemy_obj.select_attack(), choice_attack)

        if outcome == -1:
            print("You attacked successfully !\n")
            enemy_obj.decrease_lives()
            self.score += 1

        elif outcome == 1:
            print("You missed\n")
            self.decrease_lives()

        else:
            print("It's a draw\n")



