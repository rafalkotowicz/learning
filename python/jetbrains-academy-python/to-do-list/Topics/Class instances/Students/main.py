class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.student_id = name[:1] + last_name + str(birth_year)


the_name = input()
the_last_name = input()
the_birth_year = input()
student = Student(the_name, the_last_name, the_birth_year)
print(student.student_id)
