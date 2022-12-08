def main():
    section_ID_ranges = open("day4\day_4_input.txt").read().splitlines()
    overlap_count = 0

    for range_pair in section_ID_ranges:
        # split by , and -?
        # vs utilizing subsets?
        # ¯\_(ツ)_/¯

        first_range = range_pair.split(",")[0]
        second_range = range_pair.split(",")[1]
        first_range_min_max = first_range.split("-")
        second_range_min_max = second_range.split("-")
        first_range_min = int(first_range_min_max[0])
        first_range_max = int(first_range_min_max[1])
        second_range_min = int(second_range_min_max[0])
        second_range_max = int(second_range_min_max[1])

        first_range_overlaps_second = (first_range_min <= second_range_min) and (
            first_range_max >= second_range_max
        )

        second_range_overlaps_first = (second_range_min <= first_range_min) and (
            second_range_max >= first_range_max
        )

        if second_range_overlaps_first or first_range_overlaps_second:
            overlap_count += 1

    print(overlap_count)


if __name__ == "__main__":
    main()
