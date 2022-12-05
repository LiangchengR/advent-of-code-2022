def main():
    top_3_calorie_counts = [0, 0, 0]
    current_calorie_count = 0

    with open("day1\day_1_input.txt") as f:
        calories = f.read().splitlines()

    for i in range(len(calories)):
        end_of_list = i == (len(calories) - 1)

        if calories[i] == "" or end_of_list:
            if end_of_list:
                current_calorie_count += int(calories[i])

            for j in range(len(top_3_calorie_counts)):
                if current_calorie_count > top_3_calorie_counts[j]:
                    top_3_calorie_counts.insert(j, current_calorie_count)
                    top_3_calorie_counts.pop()
                    current_calorie_count = 0
                    break

            current_calorie_count = 0

        else:
            current_calorie_count += int(calories[i])

    sum_of_top_3 = sum(top_3_calorie_counts)

    return print(sum_of_top_3)
    # Answer to my puzzle was 193697


if __name__ == "__main__":
    main()
