import random


def play():
    player_position = 0
    die = random.randint(1, 6)
    play_option = random.randint(1, 3)
    if play_option == 1:
        pass
    elif play_option == 2:
        player_position -= die
    elif play_option == 3:
        player_position += die

    return play_option


if __name__ == "__main__":
    print("Welcome to snake and ladder program")
    print(play())
