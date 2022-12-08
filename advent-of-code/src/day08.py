with open('day08.txt') as f:
    lines = f.readlines()

# PART 1
# 2720 --> 1849
forest: [[int]] = []


def sanitize_line(line: str) -> str:
    return line.replace('\n', '')


def map_forest(lines) -> []:
    forest_map: [[int]] = []
    for line in lines:
        line = sanitize_line(line)
        row_of_trees: [int] = []
        for tree in list(line):
            row_of_trees.append(int(tree))
        forest_map.append(row_of_trees)
    return forest_map


def is_visible(tree_pos: (int, int), forest_map: [[int]]) -> bool:
    forest_map = forest_map
    row, col = tree_pos
    forest_width = len(forest_map)
    forest_height = len(forest_map[0])
    tree_height = forest_map[row][col]
    if row == 0 or row == forest_width - 1 or col == 0 or col == forest_height - 1:
        return True

    tree_row = forest_map[row].copy()
    west_covered: [bool] = []
    east_covered: [bool] = []
    for other_tree_col, other_tree_height in enumerate(tree_row):
        if other_tree_col < col:
            west_covered.append(other_tree_height >= tree_height)
        elif other_tree_col == col:
            continue
        else:
            east_covered.append(other_tree_height >= tree_height)

    tree_column = [forest_map[i][col] for i in range(forest_height)]
    north_covered: [bool] = []
    south_covered: [bool] = []
    for other_tree_row, other_tree_height in enumerate(tree_column):
        if other_tree_row < row:
            north_covered.append(other_tree_height >= tree_height)
        elif other_tree_row == row:
            continue
        else:
            south_covered.append(other_tree_height >= tree_height)

    # print(f'TREE: {(row, col)}')
    # print(f'N: {any(north_covered)}')
    # print(f'E: {any(east_covered)}')
    # print(f'S: {any(south_covered)}')
    # print(f'W: {any(west_covered)}')

    return not (any(west_covered) and any(east_covered) and any(south_covered) and any(north_covered))


def view_distance(tree_pos: (int, int), forest_map: [[int]]) -> int:
    forest_map = forest_map
    row_start, col_start = tree_pos
    forest_width = len(forest_map)
    forest_height = len(forest_map[0])
    tree_height = forest_map[row_start][col_start]

    if row_start == 0 or row_start == forest_width - 1 or col_start == 0 or col_start == forest_height - 1:
        return (0, 0, 0, 0)

    n_distance = 0
    for curr_row in range(row_start - 1, -1, -1):
        n_distance += 1
        other_tree_height = forest_map[curr_row][col_start]
        if other_tree_height >= tree_height:
            break

    e_distance = 0
    for curr_col in range(col_start + 1, forest_width):
        e_distance += 1
        other_tree_height = forest_map[row_start][curr_col]
        if other_tree_height >= tree_height:
            break

    s_distance = 0
    for curr_row in range(row_start + 1, forest_height):
        s_distance += 1
        other_tree_height = forest_map[curr_row][col_start]
        if other_tree_height >= tree_height:
            break

    w_distance = 0
    for curr_col in range(col_start - 1, -1, -1):
        w_distance += 1
        other_tree_height = forest_map[row_start][curr_col]
        if other_tree_height >= tree_height:
            break

    return n_distance, e_distance, s_distance, w_distance


def scenic_score(tree_pos: (int, int), forest_map: [[int]]) -> int:
    north, east, south, west = view_distance(tree_pos, forest_map)
    return north * east * south * west


def count_visible(forest_map: [[int]]) -> int:
    total_visible = 0
    tree_count = 0
    forest_width = len(forest_map)
    forest_height = len(forest_map[0])
    for row in range(forest_width):
        for col in range(forest_height):
            tree_count += 1
            if is_visible((row, col), forest_map):
                total_visible += 1

    return total_visible, tree_count


forest = map_forest(lines)


# [print(r) for r in forest]
# edges: [(int, int)] = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
#                        (1, 0), (2, 0), (3, 0), (1, 4), (2, 4), (3, 4),
#                        (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), ]
# for edge_tree in edges:
#     assert is_visible(edge_tree, forest) == True
#
# assert is_visible((1, 1), forest) == True
# assert is_visible((1, 2), forest) == True
# assert is_visible((1, 3), forest) == False
# assert is_visible((2, 1), forest) == True
# assert is_visible((2, 2), forest) == False
# assert is_visible((2, 3), forest) == True
# assert is_visible((3, 1), forest) == False
# assert is_visible((3, 2), forest) == True
# assert is_visible((3, 3), forest) == False
# assert count_visible(forest)[0] == 21
# print(f'All trees: {count_visible(forest)[1]}')
# print(f'Visible trees: {count_visible(forest)[0]}')

# Part 2, 1519245
# assert view_distance((1, 1), forest) == (1, 1, 1, 1)
# assert view_distance((1, 2), forest) == (1, 2, 2, 1)
# assert view_distance((3, 2), forest) == (2, 2, 1, 2)
# assert view_distance((3, 3), forest) == (3, 1, 1, 1)
# assert scenic_score((3, 2), forest) == 8

def get_highest_scenic_score(forest_map: [[int]]) -> int:
    scenic_scores: [int] = []
    forest_width = len(forest_map)
    forest_height = len(forest_map[0])

    for row in range(0, forest_height):
        for col in range(0, forest_width):
            scenic_scores.append(scenic_score((row, col), forest_map))

    return max(scenic_scores)


# assert get_highest_scenic_score(forest) == 8
print(get_highest_scenic_score(forest))
