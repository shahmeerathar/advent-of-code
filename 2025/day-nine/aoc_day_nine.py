import itertools


def process_inputs():
    reds = []
    with open("input.txt", "r") as file:
        for line in file:
            reds.append(tuple([int(x) for x in line.strip().split(",")]))
    return reds


def rectangle_contained(r1, r2, reds):
    top_left = [min(r1[0], r2[0]), min(r1[1], r2[1])]
    bottom_right = [max(r1[0], r2[0]), max(r1[1], r2[1])]

    for l1, l2 in itertools.pairwise(reds + [reds[0]]):
        if l1[0] == l2[0]:
            # Column line - check rect rows
            if l1[0] <= top_left[0] or l1[0] >= bottom_right[0]:
                continue

            top = min(l1[1], l2[1])
            bottom = max(l1[1], l2[1])

            if (top < top_left[1] and bottom == top_left[1]) or (
                top == bottom_right[1] and bottom > bottom_right[1]
            ):
                continue

            if (top <= top_left[1] and bottom >= top_left[1]) or (
                top <= bottom_right[1] and bottom >= bottom_right[1]
            ):
                return False
        else:
            # Row line - check rect cols
            if l1[1] <= top_left[1] or l1[1] >= bottom_right[1]:
                continue

            left = min(l1[0], l2[0])
            right = max(l1[0], l2[0])

            if (left < top_left[0] and right == top_left[0]) or (
                left == bottom_right[0] and right > bottom_right[0]
            ):
                continue

            if (left <= top_left[0] and right >= top_left[0]) or (
                left <= bottom_right[0] and right >= bottom_right[0]
            ):
                return False

    return True


def get_solution(reds: list[tuple[int, int]]):
    dimensions = [max([n[0] for n in reds]) + 1, max([n[1] for n in reds]) + 1]
    print("Dimensions: {}x{}".format(*dimensions))

    max_area = 0
    rects = []
    for p1, p2 in itertools.combinations(reds, 2):
        width = abs(p2[0] - p1[0]) + 1
        height = abs(p2[1] - p1[1]) + 1
        area = width * height
        max_area = max(max_area, area)
        rects.append((p1, p2, area))

    max_enclosed_area = 0
    rects.sort(key=lambda x: x[2], reverse=True)
    for p1, p2, area in rects:
        if rectangle_contained(p1, p2, reds):
            max_enclosed_area = area
            break

    return max_area, max_enclosed_area


if __name__ == "__main__":
    reds = process_inputs()
    solution = get_solution(reds)
    print("Part A: {}".format(solution[0]))
    print("Part B: {}".format(solution[1]))
