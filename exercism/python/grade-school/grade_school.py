"""Grade School exercise implementation."""


class School:
    """Maintain a grade-sorted school roster."""

    def __init__(self):
        self._students_by_grade = {}
        self._student_names = set()
        self._added_results = []

    def add_student(self, name, grade):
        """Try to add student; record whether adding succeeded."""
        if name in self._student_names:
            self._added_results.append(False)
            return

        students_in_grade = self._students_by_grade.setdefault(grade, set())
        students_in_grade.add(name)
        self._student_names.add(name)
        self._added_results.append(True)

    def roster(self):
        """Return all students sorted by grade and then by name."""
        result = []

        for grade_number in sorted(self._students_by_grade):
            result.extend(sorted(self._students_by_grade[grade_number]))

        return result

    def grade(self, grade_number):
        """Return all students in a given grade sorted by name."""
        return sorted(self._students_by_grade.get(grade_number, set()))

    def added(self):
        """Return add results in insertion order."""
        return list(self._added_results)
