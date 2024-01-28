def find_all_vertices(strings: [str]) -> [(int, int)]:
    vertices: [[int]] = []
    for id_y, row in enumerate(strings):
        for id_x, col in enumerate(row):
            if strings[id_y][id_x] == '+':
                vertices.append((id_y, id_x))
    return vertices


def find_all_potential_rectangles(vertices: [(int, int)], max_x: int, max_y: int) -> [(int, int), (int, int),
                                                                                      (int, int), (int, int)]:
    potential_rectangles = []
    for y in range(max_y):
        for x in range(max_x):
            for x2 in range(x + 1, max_x):
                if x >= x2:
                    continue
                else:
                    if (y, x) in vertices and (y, x2) in vertices:
                        a = (y, x)
                        b = (y, x2)
                        for y2 in range(y + 1, max_y):
                            if (y2, x) in vertices and (y2, x2) in vertices:
                                c = (y2, x)
                                d = (y2, x2)
                                potential_rectangles.append((a, b, c, d))
    return potential_rectangles


def validate_rectangles_comletness(potential_rectangles: [(int, int), (int, int),
                                                          (int, int), (int, int)], strings: [str]) -> [(int, int),
                                                                                                       (int, int),
                                                                                                       (int, int),
                                                                                                       (int, int)]:
    error_message = 'Rectangle with vertices a({}), b({}), c({}), d({}) is NOT COMPLETE (side: {})'
    complete_rectangles = []
    for potential_rectangle in potential_rectangles:
        is_complete = True
        a, b, c, d = potential_rectangle
        y = a[0]
        y2 = c[0]
        x = a[1]
        x2 = b[1]
        for curr_x in range(x + 1, x2):
            if strings[y][curr_x] not in ['-', '+']:
                print(error_message.format(a, b, c, d, 'TOP'))
                is_complete = False
                break
            if strings[y2][curr_x] not in ['-', '+']:
                print(error_message.format(a, b, c, d, 'BOTTOM'))
                is_complete = False
                break

        for curr_y in range(y + 1, y2):
            if strings[curr_y][x] not in ['|', '+']:
                print(error_message.format(a, b, c, d, 'LEFT'))
                is_complete = False
                break
            if strings[curr_y][x2] not in ['|', '+']:
                print(error_message.format(a, b, c, d, 'RIGHT'))
                is_complete = False
                break
        if is_complete:
            complete_rectangles.append(potential_rectangle)
    return complete_rectangles


# "+-+",
# "| |",
# "+-+"
# a - top left
# b - top right
# c - bottom left
# d - bottom right
def rectangles(strings: [str]) -> int:
    if not strings or len(strings) == 1:
        return 0

    max_y: int = len(strings)
    max_x: int = len(strings[0])

    vertices = find_all_vertices(strings)
    potential_rectangles = find_all_potential_rectangles(vertices, max_x, max_y)
    full_rectangles = validate_rectangles_comletness(potential_rectangles, strings)

    return len(full_rectangles)
