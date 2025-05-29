class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.hobbies = set()
        self.habits = set()

    def add_hobby(self, hobby):
        self.hobbies.add(hobby)

    def add_habit(self, habit):
        self.habits.add(habit)
