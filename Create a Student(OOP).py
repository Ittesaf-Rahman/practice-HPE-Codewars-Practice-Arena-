class student:
    def __init__(self, name , studentId):
        self.name = name
        self.studentId = studentId
        self.grade = []
    def gradeAdd(self, grade):
        self.grade.append(grade)
    def gradeAvg(self):
        if not self.grade:
            return 0
        return sum(self.grade) / len(self.grade)
student1 = student("Ittesaf", "RN0063")
student1.gradeAdd(85)
student1.gradeAdd(92)
print(f"Average grade: {student1.gradeAvg()}")