def process_inputs():
    banks = []
    with open("input.txt", "r") as file:
        for line in file:
            banks.append(line.strip())
    return banks


def joltage_recursive(bank, base, depth, cache):
    if depth == 1:
        return max([int(n) for n in bank[base:]])

    max_joltage = 0
    for i in range(len(bank) - base - depth + 1):
        if (base + i + 1, depth - 1) in cache:
            subproblem = cache[(base + i + 1, depth - 1)]
        else:
            subproblem = joltage_recursive(bank, base + i + 1, depth - 1, cache)
            cache[(base + i + 1, depth - 1)] = subproblem

        max_joltage = max(max_joltage, int("{}{}".format(bank[base + i], subproblem)))

    return max_joltage


def get_solution(banks):
    joltage_a = 0
    joltage_b = 0
    for bank in banks:
        max_joltage = 0
        for i in range(len(bank) - 1):
            for j in range(i + 1, len(bank)):
                max_joltage = max(max_joltage, int("{}{}".format(bank[i], bank[j])))
        joltage_a += max_joltage
        joltage_b = joltage_recursive(bank, 0, 12, {})

    return (joltage_a, joltage_b)


if __name__ == "__main__":
    banks = process_inputs()
    solution = get_solution(banks)
    print("Part A: {}".format(solution[0]))
    print("Part B: {}".format(solution[1]))
