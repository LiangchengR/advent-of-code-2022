def main():
    # data = open("day5\day_5_input.txt").read().splitlines()
    stacks = [
        "    [D]    ",  # 11
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
    ]
    # print(data)

    stack_map = {}

    # build map
    for stack in stacks:
        for i in range(1, len(stack), 4):
            print(stack[i])

    # Goal: After the rearrangement procedure completes, what crate ends up on top of each stack?
    # put these into arrays


if __name__ == "__main__":
    main()
