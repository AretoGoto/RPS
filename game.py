import random

MOVES = ["камень", "ножницы", "бумага"]


def computer_choice():
    return random.choice(MOVES)


def user_choice():
    while True:
        print("\n1 - камень")
        print("2 - ножницы")
        print("3 - бумага")
        print("0 - выход")

        choice = input("Твой выбор: ").strip()

        if choice == "0":
            return None

        if choice in ("1", "2", "3"):
            return MOVES[int(choice) - 1]

        print("Введите 1, 2, 3 или 0")


def determine_winner(player_move, cpu_move):
    if player_move == cpu_move:
        return "draw"

    if (
        (player_move == "камень" and cpu_move == "ножницы") or
        (player_move == "ножницы" and cpu_move == "бумага") or
        (player_move == "бумага" and cpu_move == "камень")
    ):
        return "player"

    return "pc"


def main():
    score_player = 0
    score_pc = 0

    print("\nИгра Камень ножницы бумага")
    print("\nИгра до 5 побед, попробуете победить компьютер?")

    while True:
        player_move = user_choice()
        if player_move is None:
            print("Игра завершена.")
            break

        cpu_move = computer_choice()

        print("Игрок:", player_move)
        print("Компьютер:", cpu_move)

        result = determine_winner(player_move, cpu_move)

        if result == "draw":
            print("Ничья!")
        elif result == "player":
            score_player += 1
            print("Ты победил!")
        else:
            score_pc += 1
            print("Победил компьютер!")

        print(f"Счет: Игрок {score_player} - ПК {score_pc}")

        if score_player == 5 or score_pc == 5:
            print("Игра завершена")
            break


if __name__ == "__main__":
    main()
