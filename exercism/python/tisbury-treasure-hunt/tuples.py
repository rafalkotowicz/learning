"""Bunch of helpful methods for Azara and Rui to quicker find treasures"""


def get_coordinate(record: (str, str)) -> str:
    """

    :param record: tuple - a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate: str) -> (str, str):
    """

    :param coordinate: str - a string map coordinate
    :return:  tuple - the string coordinate seperated into its individual components.
    """

    return tuple(coordinate)


def compare_records(azara_record: (str, str), rui_record: (str, (str, str), str)) -> bool:
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: bool - True if coordinates match, False otherwise.
    """

    return azara_record[1][0] == rui_record[1][0] and azara_record[1][1] == rui_record[1][1]


def create_record(azara_record: (str, str), rui_record: (str, (str, str), str)):
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return:  tuple - combined record, or "not a match" if the records are incompatible.
    """

    return azara_record + rui_record if compare_records(azara_record, rui_record) else "not a match"


def clean_up(combined_record_group):
    """

    :param combined_record_group: tuple of tuples - everything from both participants.
    :return: string of tuples separated by newlines - everything "cleaned". Excess coordinates and information removed.
    """
    report = ""
    apostrophe_found = False
    for record in combined_record_group:
        for element in record:
            if "'" in element:
                report += f"(\"{record[0]}\", '{record[2]}', ('{record[3][0]}', '{record[3][1]}'), '{record[4]}')" + "\n"
                apostrophe_found = True
                break
        if not apostrophe_found:
            report += f"('{record[0]}', '{record[2]}', ('{record[3][0]}', '{record[3][1]}'), '{record[4]}')" + "\n"

        apostrophe_found = False
    return report
