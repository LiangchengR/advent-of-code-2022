def main():
    section_ID_ranges = open("day4\day_4_input.txt").read().splitlines()
    overlap_count = 0

    for range_pair in section_ID_ranges:

        first_range = range_pair.split(",")[0]
        second_range = range_pair.split(",")[1]
        first_range_min_max = first_range.split("-")
        second_range_min_max = second_range.split("-")

        first_range_set = set(
            range(int(first_range_min_max[0]), int(first_range_min_max[1]) + 1)
        )
        second_range_set = set(
            range(int(second_range_min_max[0]), int(second_range_min_max[1]) + 1)
        )

        if first_range_set.intersection(second_range_set):
            overlap_count += 1

    print(overlap_count)


if __name__ == "__main__":
    main()
