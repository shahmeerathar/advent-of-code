def process_inputs():
    shapes = []
    regions = []

    content = None
    with open("input.txt", "r") as file:
        content = file.read()

    splits = content.split("\n\n")
    for shape in splits[:-1]:
        shapes.append([list(dim) for dim in shape.split("\n")[1:]])

    for region in splits[-1].split("\n")[:-1]:
        sections = region.split()
        dimensions = tuple(map(int, sections[0][:-1].split("x")))
        gifts = list(map(int, sections[1:]))
        regions.append((dimensions, gifts))

    return (shapes, regions)


def region_satisfied(
    shapes: list[list[str]], dimensions: tuple[int, int], shapes_required: list[int]
):
    area = dimensions[0] * dimensions[1]
    area_required = 0
    for idx, num_shape_required in enumerate(shapes_required):
        area_required += 7 * num_shape_required
    if area_required <= area:
        return True
    else:
        return False


def get_solution(
    shapes: list[list[str]], regions: list[tuple[tuple[int, int], list[int]]]
):
    regions_satisfied = 0
    for region in regions:
        if region_satisfied(shapes, region[0], region[1]):
            regions_satisfied += 1

    return regions_satisfied, 0


if __name__ == "__main__":
    shapes, regions = process_inputs()
    solution = get_solution(shapes, regions)
    print("Part A: {}".format(solution[0]))
