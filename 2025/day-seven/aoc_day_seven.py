def process_inputs():
    diagram = []
    with open("input.txt", "r") as file:
        for line in file:
            diagram.append(list(line.strip()))
    return diagram


def recurse(diagram: list[list[str]], beams: dict[int, int]):
    if len(diagram) == 1:
        return 0, sum(beams.values())

    num_splits = 0
    new_beams = {}
    for beam in beams:
        if diagram[0][beam] == "^":
            num_splits += 1
            if beam - 1 >= 0:
                new_beams[beam - 1] = new_beams.get(beam - 1, 0) + beams[beam]
            if beam + 1 < len(diagram[0]):
                new_beams[beam + 1] = new_beams.get(beam + 1, 0) + beams[beam]
        else:
            new_beams[beam] = new_beams.get(beam, 0) + beams[beam]

    for beam in new_beams:
        if diagram[1][beam] == ".":
            diagram[1][beam] = "|"

    new_splits, num_timelines = recurse(diagram[1:], new_beams)
    num_splits += new_splits

    return num_splits, num_timelines


def get_solution(diagram: list[list[str]]):
    starting = diagram[0].index("S")
    diagram[1][starting] = "|"
    bound = len(diagram)
    part_a, part_b = recurse(diagram[1:bound], {starting: 1})
    for line in diagram[:bound]:
        print("".join(line))

    return part_a, part_b


if __name__ == "__main__":
    diagram = process_inputs()
    solution = get_solution(diagram)
    print("Part A: {}".format(solution[0]))
    print("Part B: {}".format(solution[1]))
