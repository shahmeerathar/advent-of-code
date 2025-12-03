def process_inputs():
    banks = []
    with open("input.txt", "r") as file:
        for line in file:
            banks.append(line.strip())
    return banks


def joltage_recursive(bank, depth):
    if depth == 1:
        return max([int(n) for n in bank])

    max_joltage = 0
    for i in range(len(bank) - depth + 1):
        max_joltage = max(
            max_joltage,
            int("{}{}".format(bank[i], joltage_recursive(bank[i + 1 :], depth - 1))),
        )

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
        part_b = joltage_recursive(bank, 12)
        print(part_b)
        joltage_b += part_b

    return (joltage_a, joltage_b)


if __name__ == "__main__":
    banks = process_inputs()
    solution = get_solution(banks)
    print("Part A: {}".format(solution[0]))
    print("Part B: {}".format(solution[1]))
