import random
from datetime import datetime

MOVES = ["камень", "ножницы", "бумага"]


class ScoreBoard:
    def __init__(self):
        self.player_wins = 0
        self.pc_wins = 0
        self.draws = 0

    def update(self, result):
        if result == "player":
            self.player_wins += 1
        elif result == "pc":
            self.pc_wins += 1
        else:
            self.draws += 1

    def display(self):
        print(f"Счет: Игрок {self.player_wins} - ПК {self.pc_wins} (Ничьи: {self.draws})")

    def save_to_file(self, filename="scores.txt"):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"{now} | player={self.player_wins} pc={self.pc_wins} draws={self.draws}\n")


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
    score = ScoreBoard()

    print("\nИгра Камень ножницы бумага")
    print("\nИгра до 5 побед, попробуете победить компьютер?")

    while True:
        player_move = user_choice()
        if player_move is None:
            print("Игра завершена.")
            score.display()
            score.save_to_file()
            print("Результат сохранен в scores.txt")
            break

        cpu_move = computer_choice()

        print("Игрок:", player_move)
        print("Компьютер:", cpu_move)

        result = determine_winner(player_move, cpu_move)

        if result == "draw":
            print("Ничья!")
        elif result == "player":
            print("Ты победил!")
        else:
            print("Победил компьютер!")

        score.update(result)
        score.display()

        if score.player_wins == 5 or score.pc_wins == 5:
            print("Игра завершена")
            score.display()
            score.save_to_file()
            print("Результат сохранен в scores.txt")
            break


if __name__ == "__main__":
    main()
