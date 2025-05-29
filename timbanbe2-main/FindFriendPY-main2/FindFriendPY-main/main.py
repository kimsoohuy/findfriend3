from dataloader import load_students, load_hobbies, load_habits, load_edges
from graph import Graph
from recommender import Recommender
import listing  

def show_menu():
    print("=== MENU ===")
    print("1. Thêm bạn")
    print("2. Xóa bạn")
    print("3. Gợi ý bạn bè")
    print("4. Liệt kê danh sách toàn bộ người dùng")
    print("5. Thoát")

def main():
    # đường dẫn data tuỳ theo máy bạn
    students = load_students(r'E:\timbanbe2-main\timbanbe2-main\FindFriendPY-main2\FindFriendPY-main\data\student_info.txt')
    load_hobbies(r'E:\timbanbe2-main\timbanbe2-main\FindFriendPY-main2\FindFriendPY-main\data\hobbyc.txt', students)
    load_habits(r'E:\timbanbe2-main\timbanbe2-main\FindFriendPY-main2\FindFriendPY-main\data\habitc.txt', students)

    graph = Graph()
    load_edges(r'E:\timbanbe2-main\timbanbe2-main\FindFriendPY-main2\FindFriendPY-main\data\friends.txt', graph)

    recommender = Recommender(graph, students)

    user_id = input("Nhập mã số sinh viên để tìm bạn bè: ").strip()
    if user_id not in students:
        print(f"Mã số sinh viên '{user_id}' không hợp lệ.")
        return

    while True:
        show_menu()
        choice = input("Chọn (1-5): ").strip()

        if choice == '1':
            other = input("Nhập MSSV bạn muốn thêm: ").strip()
            if other in students:
                graph.add_edge(user_id, other)
                print(f"✔ Đã thêm bạn: {students[other].name} (MSSV {other})")
            else:
                print(f"[!] MSSV '{other}' không hợp lệ.")

        elif choice == '2':
            other = input("Nhập MSSV bạn muốn xóa: ").strip()
            if other in students:
                if other in graph.neighbors(user_id):
                    graph.remove_edge(user_id, other)
                    print(f"✔ Đã xóa bạn: {students[other].name} (MSSV {other})")
                else:
                    print(f"[!] {students[other].name} (MSSV {other}) hiện không phải là bạn của bạn.")
            else:
                print(f"[!] MSSV '{other}' không hợp lệ.")

        elif choice == '3':
            recs = recommender.recommend_friends(user_id)
            print(f"\nGợi ý bạn bè cho {students[user_id].name} (MSSV {user_id}):")
            if not recs:
                print("Không có gợi ý mới.")
            else:
                for rid, score in recs:
                    name = students[rid].name if rid in students else rid
                    print(f"- {name} (MSSV {rid}) (Điểm: {score:.1f}/10)")

        elif choice == '4':
            # gọi hàm liệt kê từ listing.py
            listing.list_users(students)

        elif choice == '5':
            print("Thoát chương trình. Hẹn gặp lại!")
            break

        else:
            print("[!] Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()
