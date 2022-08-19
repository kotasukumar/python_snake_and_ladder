import random


def play():
    player_position = 0
    while player_position != 100:
        die = random.randint(1, 6)
        play_option = random.randint(1, 3)
        if play_option == 1:
            pass
        elif play_option == 2:
            player_position -= die
        elif play_option == 3:
            player_position += die
        if player_position < 0:
            player_position = 0
        elif player_position > 100:
            player_position -= die
        elif player_position == 100:
            break

    return player_position


if __name__ == "__main__":
    print("Welcome to snake and ladder program")
    print(play())
