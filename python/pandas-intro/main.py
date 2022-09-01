import pandas
import numpy


def test_insert_to_postgres():
    columns: [str] = ["id", "name", "is_active"]
    data: [(int, str, bool)] = [
        (1, "User 1", True),
        (2, "User 2", False),
        (3, "User 3", None)
    ]

    dataFrame = pandas.DataFrame(data, columns=columns)
    print("\n")
    print(dataFrame)
