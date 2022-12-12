def main():
    crate_stacks = generate_stacks_and_procedure()["stacks"]
    procedure = generate_stacks_and_procedure()["procedure"]

    sorted_stacks = execute_stack_procedure(crate_stacks, procedure)

    for stack in sorted_stacks:
        print(stack[-1])


def generate_stacks_and_procedure():
    data = open("day5\day_5_input.txt").read().splitlines()
    # data = [
    #     "    [D]    ",  # 11
    #     "[N] [C]    ",
    #     "[Z] [M] [P]",
    #     " 1   2   3 ",
    #     "",
    #     "move 1 from 2 to 1",
    #     "move 3 from 1 to 3",
    #     "move 2 from 2 to 1",
    #     "move 1 from 1 to 2",
    # ]
    # print(data)

    crate_stacks = []
    is_initializing_new_stacks = True
    procedure_index = 0

    for crate_row in range(0, len(data)):
        if len(data[crate_row]) == 0:
            procedure_index = crate_row + 1
            break

        if crate_row == 1:
            is_initializing_new_stacks = False

        stack_index = 0
        for crate_index in range(1, len(data[crate_row]), 4):
            crate_label = data[crate_row][crate_index]

            if is_initializing_new_stacks:
                crate_stacks.append(list(crate_label))

            else:
                crate_stacks[stack_index].insert(0, crate_label)
                stack_index += 1

    stripped_crate_stacks = [
        [crate for crate in crate_stack if crate != " "] for crate_stack in crate_stacks
    ]

    return {"stacks": stripped_crate_stacks, "procedure": data[procedure_index:]}


def execute_stack_procedure(stacks, procedure):

    for instruction_string in procedure:
        quantity = int(instruction_string.split(" ")[1])
        from_stack_index = int(instruction_string.split(" ")[3]) - 1
        to_stack_index = int(instruction_string.split(" ")[5]) - 1

        crates_to_move = stacks[from_stack_index][-quantity:]
        for crate in crates_to_move:
            stacks[to_stack_index].append(crate)

        for i in range(0, quantity):
            stacks[from_stack_index].pop()

    return stacks


if __name__ == "__main__":
    main()
