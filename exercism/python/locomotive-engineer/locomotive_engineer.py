"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*ids: list | tuple) -> [int]:
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(ids)


def fix_list_of_wagons(each_wagons_id: [int], missing_wagons: [int]) -> [int]:
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    result: [int] = []
    second_to_last, last, first, *in_order = each_wagons_id
    result.append(first)
    result.extend(missing_wagons)
    result.extend(in_order)
    result.append(second_to_last)
    result.append(last)

    return result


def add_missing_stops(from_to: dict, **stops: dict) -> dict:
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    route_with_stops: dict = dict(from_to)
    route_with_stops['stops'] = list(stops.values())

    return route_with_stops


def extend_route_information(route: dict, more_route_information: dict) -> dict:
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows: list[list[tuple]]) -> list[list[tuple]]:
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    colour_1, colour_2, colour_3 = wagons_rows
    c_1_1, c_1_2, c_1_3 = colour_1
    c_2_1, c_2_2, c_2_3 = colour_2
    c_3_1, c_3_2, c_3_3 = colour_3
    return [
        [c_1_1, c_2_1, c_3_1],
        [c_1_2, c_2_2, c_3_2],
        [c_1_3, c_2_3, c_3_3]
    ]
