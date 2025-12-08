import itertools


def process_inputs():
    junctions = []
    with open("input.txt", "r") as file:
        for line in file:
            junctions.append(tuple([int(coord) for coord in line.strip().split(",")]))
    return junctions


def distance(v1: tuple[int], v2: tuple[int]):
    dist = 0
    for coord1, coord2 in zip(v1, v2):
        dist += pow(coord2 - coord1, 2)
    return pow(dist, 0.5)


def find_circuits(circuits, j1, j2):
    circuit_with_first = -1
    circuit_with_second = -1
    for idx, circuit in enumerate(circuits):
        if j1 in circuit:
            circuit_with_first = idx
        if j2 in circuit:
            circuit_with_second = idx

    return circuit_with_first, circuit_with_second


def get_solution(junctions: list[tuple[int]]):
    part_a = 1
    part_b = 0

    distances = [
        (combo, distance(*combo)) for combo in itertools.combinations(junctions, 2)
    ]
    distances.sort(key=lambda x: x[1])

    idx = 0
    circuits: list[set[tuple[int]]] = [set([junction]) for junction in junctions]
    circuits_part_a: list[set[tuple[int]]] = []
    while len(circuits) > 1:
        if idx == 1000:
            circuits_part_a = circuits.copy()

        min_combo, min_distance = distances[idx]
        idx += 1

        p1, p2 = find_circuits(circuits, min_combo[0], min_combo[1])
        if p1 == p2:
            continue

        # Merge circuits
        circuits[p1] = circuits[p1].union(circuits[p2])
        circuits.pop(p2)
        circuits.sort(key=len, reverse=True)

    for circuit in circuits_part_a[:3]:
        part_a *= len(circuit)

    part_b = min_combo[0][0] * min_combo[1][0]
    return part_a, part_b


if __name__ == "__main__":
    junctions = process_inputs()
    solution = get_solution(junctions)
    print("Part A: {}".format(solution[0]))
    print("Part B: {}".format(solution[1]))
