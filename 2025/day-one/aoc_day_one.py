def process_inputs():
    inputs = []
    with open("input.txt", "r") as file:
        for line in file:
            inputs.append(line.strip())
    return inputs


def get_solution(inputs):
    curr_num = 50
    times_ended_at_zero = 0
    total_zero_encounters = 0

    for input in inputs:
        dir = input[0]
        distance = int(input[1:])
        if dir == "L":
            distance *= -1

        pre_mod = curr_num + distance
        if pre_mod <= 0:
            # Only possible when crossing 0 while turning left
            pre_mod = -1 * pre_mod
            if curr_num != 0:
                # Avoid double counting
                pre_mod += 100
        total_zero_encounters += pre_mod // 100

        curr_num = (curr_num + distance) % 100
        if curr_num == 0:
            times_ended_at_zero += 1

        print(
            "{:<4} {:<4} {:<4} {:<4} {:<4}".format(
                input, pre_mod, curr_num, times_ended_at_zero, total_zero_encounters
            )
        )

    return (times_ended_at_zero, total_zero_encounters)


if __name__ == "__main__":
    inputs = process_inputs()
    solution = get_solution(inputs)
    print(solution)
    print("Part A (times ended at 0): {}".format(solution[0]))
    print("Part B (total zero encounters): {}".format(solution[1]))
