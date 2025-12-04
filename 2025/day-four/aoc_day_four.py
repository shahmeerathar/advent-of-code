def process_inputs():
    layout = []
    with open("input.txt", "r") as file:
        for line in file:
            row = [c for c in line.strip()]
            print(row)
            layout.append(row)

    return layout


def get_solution(layout):
    part_a = 0
    part_b = 0

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

            print("{} {} {}".format(y, x, num_surrounding_rolls))
            if num_surrounding_rolls < 4:
                part_a += 1

    return (part_a, part_b)


if __name__ == "__main__":
    layout = process_inputs()
    solution = get_solution(layout)
    print("Part A: {}".format(solution[0]))
    print("Part B: {}".format(solution[1]))
