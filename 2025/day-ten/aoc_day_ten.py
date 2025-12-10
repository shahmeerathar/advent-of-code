from tqdm import tqdm


def process_inputs():
    inputs = []
    with open("input.txt", "r") as file:
        for line in file:
            chunks = line.strip().split(" ")
            lights = list(chunks[0][1:-1])
            lights = list(map(lambda x: 1 if x == "#" else 0, chunks[0][1:-1]))
            buttons = [
                tuple([int(c) for c in button[1:-1].split(",")])
                for button in chunks[1:-1]
            ]
            joltages = [int(joltage) for joltage in chunks[-1][1:-1].split(",")]
            inputs.append((lights, buttons, joltages))

    return inputs


def helper_lights(state, expected, buttons, depth):
    if depth == 0:
        return state == expected

    possible = False
    for button in buttons:
        new_state = state.copy()
        for light in button:
            new_state[light] = 1 - new_state[light]
        possible = possible or helper_lights(new_state, expected, buttons, depth - 1)

    return possible


def min_presses_lights(data):
    minimum = 1
    while True:
        possible = helper_lights([0] * len(data[0]), data[0], data[1], minimum)
        if possible:
            return minimum

        minimum += 1


def helper_joltages(state, expected, buttons, depth):
    if depth == 0:
        return state == expected

    possible = False
    for button in buttons:
        new_state = state.copy()
        for joltage in button:
            new_state[joltage] += 1
        exceeds = False
        for a, b in zip(new_state, expected):
            if a > b:
                exceeds = True
                break
        if exceeds:
            continue
        possible = possible or helper_joltages(new_state, expected, buttons, depth - 1)

    return possible


def min_presses_joltages(data):
    minimum = 1
    while True:
        possible = helper_joltages([0] * len(data[0]), data[2], data[1], minimum)
        if possible:
            return minimum

        minimum += 1


def get_solution(inputs):
    total_presses_lights = 0
    total_presses_joltages = 0
    for inp in tqdm(inputs):
        total_presses_lights += min_presses_lights(inp)
    for inp in tqdm(inputs):
        total_presses_joltages += min_presses_joltages(inp)

    return total_presses_lights, total_presses_joltages


if __name__ == "__main__":
    inputs = process_inputs()
    solution = get_solution(inputs)
    print("Part A: {}".format(solution[0]))
    print("Part B: {}".format(solution[1]))
