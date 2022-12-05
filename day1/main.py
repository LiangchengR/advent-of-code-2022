def main():
    highest_calorie_count = 0
    current_calorie_count = 0

    with open("day1\day_1_input.txt") as f:
        calories = f.read().splitlines()

    for i in range(len(calories)):
        if calories[i]:
            current_calorie_count += int(calories[i])

        else:
            if current_calorie_count > highest_calorie_count:
                highest_calorie_count = current_calorie_count
                current_calorie_count = 0
            else:
                current_calorie_count = 0

    return print(highest_calorie_count)


if __name__ == "__main__":
    main()
