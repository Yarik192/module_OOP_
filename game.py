"""MAIN LOGIC FOR GAME"""
from models import *


def play():

    player = get_player_instance()
    enemy = get_enemy_instance()

    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)

        except EnemyDown:
            player.score += 5
            enemy = get_enemy_instance(enemy.level + 1)

        except GameOver:
            get_scores(player)
            raise KeyboardInterrupt


if __name__ == '__main__':
    try:
        play()
    except KeyboardInterrupt:
        pass
    finally:
        print("Good Bye!")

