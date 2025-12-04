def process_inputs():
    layout = set()
    with open("input.txt", "r") as file:
        for y, line in enumerate(file):
            for x, c in enumerate(line.strip()):
                if c == "@":
                    layout.add((y, x))

    return layout


def move_rolls(layout: set):
    rolls_moved = 0
    new_layout = set()

    for y, x in layout:
        num_surrounding_rolls = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == 0 and dx == 0:
                    continue

                if (y + dy, x + dx) in layout:
                    num_surrounding_rolls += 1

        if num_surrounding_rolls >= 4:
            new_layout.add((y, x))
        else:
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
