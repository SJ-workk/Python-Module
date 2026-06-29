class StudentResult:
    def __init__(self, name, age, average_grade):
        self.name = name
        self.age = age
        self.average_grade = average_grade

    def has_passed(self):
        return self.average_grade >= 50


students = [
    StudentResult("John", 22, 45),
    StudentResult("Emma", 20, 78),
    StudentResult("Sam", 21, 55),
]

for s in students:
    if s.has_passed():
        print(s.name)