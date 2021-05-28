# The following code is needed for us to check your answer, do not modify it, please.
students = json.loads(input())
Belov = students['Belov']
Smith = students['Smith']
Sarada = students['Sarada']

# Belov = ["Physics", "Math", "Russian"]
# Smith = ["Math", "Geometry", "English"]
# Sarada = ["Japanese", "Math", "Physics"]

subjects = set()
subjects.update(Belov)
subjects.update(Smith)
subjects.update(Sarada)

print(len(subjects))
