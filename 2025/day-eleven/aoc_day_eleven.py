def process_inputs():
    graph = {}
    with open("input.txt", "r") as file:
        for line in file:
            split = line.strip().split()
            graph[split[0][:-1]] = split[1:]

    return graph


def recurse(
    graph: dict[str, list[str]],
    current_node: str,
    cache: dict[tuple[str, int], int] = {},
    required: set[str] = set(),
    num_required_found: int = 0,
):
    if current_node == "out":
        if num_required_found == len(required):
            # Assumes no cycles
            return 1
        else:
            return 0

    total_paths = 0
    for child in graph[current_node]:
        child_num_required_found = num_required_found
        if child in required:
            child_num_required_found += 1

        if (child, child_num_required_found) in cache:
            total_paths += cache[(child, child_num_required_found)]
        else:
            paths_for_child = recurse(
                graph, child, cache, required, child_num_required_found
            )

            cache[(child, child_num_required_found)] = paths_for_child
            total_paths += paths_for_child

    return total_paths


def get_solution(graph: dict[str, list[str]]):
    num_paths = recurse(graph, "you")
    num_paths_with_dac_and_fft = recurse(graph, "svr", {}, set(["dac", "fft"]))
    return num_paths, num_paths_with_dac_and_fft


if __name__ == "__main__":
    graph = process_inputs()
    solution = get_solution(graph)
    print("Part A: {}".format(solution[0]))
    print("Part B: {}".format(solution[1]))
