def process_inputs():
    a_tmp = []
    b_tmp = []
    homework_a = []
    homework_b = []

    with open("input.txt", "r") as file:
        for line in file:
            elements = line.strip().split()
            a_tmp.append(elements)
            b_tmp.append(line.strip("\n"))

    homework_a = [list(row) for row in zip(*a_tmp)]

    problem_num = 0
    problem = []
    for x in range(len(b_tmp[0])):
        digits = []
        for y in range(len(b_tmp) - 1):
            digit = b_tmp[y][x]
            if digit != " ":
                digits.append(digit)

        if len(digits) == 0:
            # start of next problem
            problem.append(homework_a[problem_num][-1])
            homework_b.append(problem)
            problem_num += 1
            problem = []
            continue

        num = "".join(digits)
        problem.append(num)

    problem.append(homework_a[problem_num][-1])
    homework_b.append(problem)

    return homework_a, homework_b


def get_solution(homework):
    answer = 0
    for problem in homework:
        operator = problem[-1]
        sol = 0 if operator == "+" else 1
        for operand in problem[:-1]:
            if operator == "+":
                sol += int(operand)
            else:
                sol *= int(operand)
        answer += sol

    return answer


if __name__ == "__main__":
    homework_a, homework_b = process_inputs()
    solution = get_solution(homework_a), get_solution(homework_b)
    print("Part A: {}".format(solution[0]))
    print("Part B: {}".format(solution[1]))
