from models import Student

def load_students(filepath):
    students = {}
    with open(filepath, encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(maxsplit=1)
            if len(parts) == 2:
                id, name = parts
                students[id] = Student(id, name)
    return students

def load_hobbies(filepath, students):
    with open(filepath, encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(maxsplit=1)
            if len(parts) == 2:
                id, hobby = parts
                if id in students:
                    students[id].add_hobby(hobby)

def load_habits(filepath, students):
    with open(filepath, encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(maxsplit=1)
            if len(parts) == 2:
                id, habit = parts
                if id in students:
                    students[id].add_habit(habit)


def load_edges(filepath, graph):
    with open(filepath, encoding='utf-8') as f:
        for line in f:
            u, v = line.strip().split()
            graph.add_edge(u, v)
