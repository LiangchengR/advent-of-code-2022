def main():
    highest_calorie_count = 0
    current_calorie_count = 0

    with open("day1\day_1_input.txt") as f:
        calories = f.read().splitlines()

    for i in range(len(calories)):
        end_of_list = i == (len(calories) - 1)

        if calories[i] == "" or end_of_list:
            if end_of_list:
                current_calorie_count += int(calories[i])

            if current_calorie_count > highest_calorie_count:
                highest_calorie_count = current_calorie_count
                current_calorie_count = 0
            else:
                current_calorie_count = 0

        else:
            current_calorie_count += int(calories[i])

    return print(highest_calorie_count)
    # Answer to my puzzle was 64929


if __name__ == "__main__":
    main()
