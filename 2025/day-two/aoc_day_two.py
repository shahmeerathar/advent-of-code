import re


def process_inputs():
    ranges = []
    with open("input.txt", "r") as file:
        ranges = [
            [int(n) for n in r.split("-")] for r in file.readline().strip().split(",")
        ]
    return ranges


def is_invalid_part_a(id):
    if len(id) % 2 == 1:
        return False

    if id[: len(id) // 2] == id[len(id) // 2 :]:
        return True

    return False


def is_invalid_part_b(id):
    use_regex = False

    if use_regex:
        x = re.search(r"^(.+)\1+$", id)
        return x is not None
    else:
        # k = bucket size
        for k in range(1, len(id) // 2 + 1):
            if len(id) % k != 0:
                # buckets not all equally sized
                continue
            valid = False
            for n in range(len(id) // k):
                # iterate over buckets
                if id[n * k : n * k + k] != id[:k]:
                    valid = True
                    break
            if not valid:
                return True

        return False


def get_solution(ranges):
    sum_a = 0
    sum_b = 0
    for r in ranges:
        start = r[0]
        end = r[1]

        for i in range(start, end + 1):
            if is_invalid_part_a(str(i)):
                sum_a += i
            if is_invalid_part_b(str(i)):
                sum_b += i

    return (sum_a, sum_b)


if __name__ == "__main__":
    ranges = process_inputs()
    solution = get_solution(ranges)
    print("Part A: {}".format(solution[0]))
    print("Part B: {}".format(solution[1]))
