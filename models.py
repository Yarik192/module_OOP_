"""CLASS PLAYER AND ENEMY FOR GAME"""

import random
from settings import LIVES, exodus_1, exodus_2, rules
from exeptions import GameOver, EnemyDown


class Enemy:
    def __init__(self, level: int):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack() -> int:
        return random.randint(1, 3)

    def decrease_lives(self) -> None:
        if self.lives != 0:
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
        if self.lives != 1:
            self.lives -= 1
            print(f"You have {self.lives} lives left\n")
        else:
            print(f"You scored: {self.score}")
            raise GameOver

    def attack(self, enemy_obj: Enemy) -> None:
        while True:
            choice_attack = int(input("Choose who you want to attack: "))
            outcome = self.fight(choice_attack, enemy_obj.select_attack())
            if outcome == 0:
                print("It's a draw\n")
            elif outcome == -1:
                print("You missed\n")
                self.decrease_lives()
            elif outcome == 1:
                print("You attacked successfully !\n")
                enemy_obj.decrease_lives()
                self.score += 1
            break

    def defence(self, enemy_obj: Enemy) -> None:
        while True:
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
            break


def get_player_instance() -> Player:
    user_name = input("Enter your name: ")
    while True:
        choice = input("Enter start for start the game: ")
        if choice == "start":
            break
        continue
    rules()
    return Player(user_name)


def get_enemy_instance(lvl=1) -> Enemy:
    return Enemy(lvl)


def get_scores(player_obj: Player) -> None:
    with open("scores.txt", "a") as score:
        score.write(f"Player - {player_obj.name}, scored: {player_obj.score} points\n")
