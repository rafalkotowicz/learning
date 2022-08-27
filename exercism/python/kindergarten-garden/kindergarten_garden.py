ALL_STUDENTS = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid",
                "Larry"]


class Garden:
    plant_dict = {
        "C": "Clover",
        "G": "Grass",
        "R": "Radishes",
        "V": "Violets"
    }

    def __init__(self, diagram: str, students=ALL_STUDENTS):
        self.rows = diagram.split("\n")
        self.students = sorted(students)

    def plants(self, student_name: str) -> [str]:
        student_id: int = self.students.index(student_name)
        return [Garden.plant_dict[plant]
                for row in self.rows
                for plant in row[student_id * 2:student_id * 2 + 2]]
