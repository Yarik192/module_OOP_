"""MAIN LOGIC FOR GAME"""
from models import *


def get_scores(player_obj: Player) -> None:
    with open("scores.txt", "a") as score:
        score.write(f"Player - {player_obj.name}, scored: {player_obj.score} points\n")


def get_player_instance() -> Player:
    user_name = input("Enter your name: ")
    while not user_name:
        user_name = input("Enter your name")
    choice = input("Enter start for start the game: ")
    if choice == "start":
        return Player(user_name)


def get_enemy_instance(level=1):
    return Enemy(level)


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


def play():

    player = get_player_instance()
    enemy = get_enemy_instance()
    rules()
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

