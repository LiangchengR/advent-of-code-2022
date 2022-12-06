def main():
    moves = open("day2\day_2_input.txt").read().splitlines()

    game_outcomes = {
        "X": {"A": "C", "B": "A", "C": "B"},
        "Y": {"A": "A", "B": "B", "C": "C"},
        "Z": {"A": "B", "B": "C", "C": "A"},
    }
    move_values = {"A": 1, "B": 2, "C": 3}
    outcome_values = {"X": 0, "Y": 3, "Z": 6}
    total_score = 0

    for move in moves:
        desired_outcome = move[-1]
        oponent_move = move[0]
        my_move = game_outcomes[desired_outcome][oponent_move]

        total_score += outcome_values[desired_outcome]
        total_score += move_values[my_move]

    print(total_score)


if __name__ == "__main__":
    main()
