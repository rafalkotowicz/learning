"""Build a closed domino chain when possible."""

def _build_graph(dominoes):
    adjacency = {}
    degree = {}
    for index, (left, right) in enumerate(dominoes):
        adjacency.setdefault(left, []).append((index, right))
        adjacency.setdefault(right, []).append((index, left))
        degree[left] = degree.get(left, 0) + 1
        degree[right] = degree.get(right, 0) + 1
    return adjacency, degree


def _all_even_degrees(degree):
    return all(not count % 2 for count in degree.values())


def _non_isolated_vertices(degree):
    return [vertex for vertex, count in degree.items() if count > 0]


def _connected_vertices(start, adjacency):
    visited = set()
    stack = [start]
    while stack:
        if (vertex := stack.pop()) in visited:
            continue
        visited.add(vertex)
        for edge in adjacency.get(vertex, []):
            if (neighbor := edge[1]) not in visited:
                stack.append(neighbor)
    return visited


def _build_eulerian_vertex_path(start, adjacency):
    used_edges = set()
    traversal_stack = [start]
    vertex_path = []
    while traversal_stack:
        current = traversal_stack[-1]
        next_edge = None
        for edge_id, neighbor in adjacency.get(current, []):
            if edge_id not in used_edges:
                next_edge = (edge_id, neighbor)
                break
        if next_edge is None:
            vertex_path.append(traversal_stack.pop())
        else:
            edge_id, neighbor = next_edge
            used_edges.add(edge_id)
            traversal_stack.append(neighbor)
    return vertex_path, used_edges


def _vertex_path_to_chain(vertex_path):
    return [
        (vertex_path[index], vertex_path[index + 1])
        for index in range(len(vertex_path) - 1)
    ]


def can_chain(dominoes):
    """Return a valid closed chain using all dominoes, or None."""
    if not dominoes:
        return []

    adjacency, degree = _build_graph(dominoes)
    if not _all_even_degrees(degree):
        return None

    if not (non_isolated := _non_isolated_vertices(degree)):
        return []

    start = non_isolated[0]
    visited_vertices = _connected_vertices(start, adjacency)
    is_valid = not any(vertex not in visited_vertices for vertex in non_isolated)
    chain = None

    if is_valid:
        vertex_path, used_edges = _build_eulerian_vertex_path(start, adjacency)
        is_valid = len(used_edges) == len(dominoes)

    if is_valid:
        vertex_path.reverse()
        is_valid = len(vertex_path) == len(dominoes) + 1

    if is_valid:
        chain = _vertex_path_to_chain(vertex_path)
        is_valid = not chain or chain[0][0] == chain[-1][1]

    return chain if is_valid else None
