def process_inputs():
    ranges = []
    available = []
    with open("input.txt", "r") as file:
        populate_ranges = True
        for line in file:
            if len(line.strip()) == 0:
                populate_ranges = False
                continue

            if populate_ranges:
                ranges.append([int(bound) for bound in line.strip().split("-")])
            else:
                available.append(int(line.strip()))

    return ranges, available


def get_solution(ranges, available):
    part_a = 0
    part_b = 0

    for item in available:
        fresh = False
        for r in ranges:
            if item in range(r[0], r[1] + 1):
                fresh = True
                break

        if fresh:
            part_a += 1

    ranges.sort(key=lambda x: x[0])
    range_start = ranges[0][0]
    range_end = ranges[0][1]
    for r in ranges[1:]:
        if r[0] <= range_end:
            range_end = max(range_end, r[1])
        else:
            part_b += range_end - range_start + 1
            range_start = r[0]
            range_end = r[1]
    part_b += range_end - range_start + 1

    return (part_a, part_b)


if __name__ == "__main__":
    ranges, available = process_inputs()
    solution = get_solution(ranges, available)
    print("Part A: {}".format(solution[0]))
    print("Part B: {}".format(solution[1]))
