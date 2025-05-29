# listing.py

def list_users(students):
    """
    In ra danh sách toàn bộ người dùng.
    students: dict mapping MSSV -> Student object (có thuộc tính .name)
    """
    print("\n=== Danh sách toàn bộ người dùng ===")
    for mssv, student in students.items():
        print(f"- {student.name} (MSSV {mssv})")
    print()
