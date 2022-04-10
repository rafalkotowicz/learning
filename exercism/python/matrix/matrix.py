class Matrix:
    matrix = []

    def __init__(self, matrix_string: str):
        matrix = []
        for row in str.split(matrix_string, sep="\n"):
            row_data = []
            for column in row.split(sep=" "):
                row_data.append(int(column))
            matrix.append(row_data)
        self.matrix = matrix

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]
