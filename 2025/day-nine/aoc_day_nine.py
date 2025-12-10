import itertools
import math
import numpy as np
from tqdm import tqdm
from scipy import ndimage
from pathlib import Path


def process_inputs():
    reds = []
    with open("input.txt", "r") as file:
        for line in file:
            reds.append(tuple([int(x) for x in line.strip().split(",")]))
    return reds


def get_solution(reds: list[tuple[int, int]]):
    part_a = 0
    part_b = 0

    dimensions = [max([n[0] for n in reds]) + 1, max([n[1] for n in reds]) + 1]
    print("Dimensions: {}x{}".format(*dimensions))

    # Build outline
    print("Building outline")
    grid = np.zeros(dimensions)
    for p1, p2 in itertools.pairwise(reds + [reds[0]]):
        if p1[0] == p2[0]:
            start, end = min(p1[1], p2[1]), max(p1[1], p2[1])
            grid[p1[0], start : end + 1] = 1
        if p1[1] == p2[1]:
            start, end = min(p1[0], p2[0]), max(p1[0], p2[0])
            grid[start : end + 1, p1[1]] = 1

    # Fill in
    print("Filling in")
    file = "filled.npy"
    if Path(file).exists():
        print("Loading file")
        filled = np.load(file)
    else:
        filled = ndimage.binary_fill_holes(grid).astype(int)
        np.save(file, filled)

    max_area = 0
    rects = []
    for p1, p2 in tqdm(itertools.combinations(reds, 2), total=math.comb(len(reds), 2)):
        width = abs(p2[0] - p1[0]) + 1
        height = abs(p2[1] - p1[1]) + 1
        area = width * height
        max_area = max(max_area, area)
        rects.append((p1, p2, area))

    max_enclosed_area = 0
    rects.sort(key=lambda x: x[2], reverse=True)
    for p1, p2, area in tqdm(rects):
        top_left = [min(p1[0], p2[0]), min(p1[1], p2[1])]
        bottom_right = [max(p1[0], p2[0]), max(p1[1], p2[1])]
        rect = filled[
            top_left[0] : bottom_right[0] + 1, top_left[1] : bottom_right[1] + 1
        ]
        if np.all(rect == 1):
            max_enclosed_area = area
            break

    part_a = max_area
    part_b = max_enclosed_area
    return part_a, part_b


if __name__ == "__main__":
    reds = process_inputs()
    solution = get_solution(reds)
    print("Part A: {}".format(solution[0]))
    print("Part B: {}".format(solution[1]))
