def main():
    games = open("day2\day_2_input.txt").read().splitlines()

    move_values = {"X": 1, "Y": 2, "Z": 3}
    game_outcomes = {
        "loss": ["A Z", "B X", "C Y"],
        "draw": ["A X", "B Y", "C Z"],
        "win": ["A Y", "B Z", "C X"],
    }
    outcome_values = {"loss": 0, "draw": 3, "win": 6}
    total_score = 0

    for move in games:
        total_score += move_values[move[-1]]

        if move in game_outcomes["win"]:
            total_score += outcome_values["win"]

        elif move in game_outcomes["loss"]:
            total_score += outcome_values["loss"]

        else:
            total_score += outcome_values["draw"]

    print(total_score)


if __name__ == "__main__":
    main()
