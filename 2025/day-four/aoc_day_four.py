import copy


def process_inputs():
    layout = []
    with open("input.txt", "r") as file:
        for line in file:
            row = [c for c in line.strip()]
            layout.append(row)

    return layout


def move_rolls(layout):
    rolls_moved = 0
    new_layout = copy.deepcopy(layout)

    for row in layout:
        print(row)

    for y in range(len(layout)):
        for x in range(len(layout[0])):
            if layout[y][x] != "@":
                continue
            num_surrounding_rolls = 0
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    adjacent_pos = (y + dy, x + dx)
                    if (
                        adjacent_pos[0] < 0
                        or adjacent_pos[0] >= len(layout)
                        or adjacent_pos[1] < 0
                        or adjacent_pos[1] >= len(layout[0])
                        or (dy == 0 and dx == 0)
                    ):
                        continue

                    if layout[adjacent_pos[0]][adjacent_pos[1]] == "@":
                        num_surrounding_rolls += 1

            if num_surrounding_rolls < 4:
                new_layout[y][x] = "x"
                rolls_moved += 1

    print("Moved {} rolls".format(rolls_moved))
    return rolls_moved, new_layout


def get_solution(layout):
    part_a, layout = move_rolls(layout)
    part_b = part_a
    while True:
        delta, layout = move_rolls(layout)
        if delta == 0:
            break
        part_b += delta

    return (part_a, part_b)


if __name__ == "__main__":
    layout = process_inputs()
    solution = get_solution(layout)
    print("Part A: {}".format(solution[0]))
    print("Part B: {}".format(solution[1]))
