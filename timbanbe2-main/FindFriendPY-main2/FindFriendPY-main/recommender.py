class Recommender:
    def __init__(self, graph, students):
        self.graph = graph
        self.students = students

    def recommend_friends(self, user_id, max_results=3, w_mutual=0.3, w_hobby=0.5, w_habit=0.2):
        # 1. Kiểm tra user có trong graph không
        if not self.graph.has_node(user_id):
            return []

        # 2. Lấy tập bạn trực tiếp của user
        friends = self.graph.neighbors(user_id)
        friends_set = set()
        for f in friends:
            friends_set.add(f)

        # 3. Lấy thông tin user
        if user_id in self.students:
            user = self.students[user_id]
        else:
            return []

        # 4. Khởi tạo dict để đếm số bạn chung, sở thích chung, thói quen chung
        mutual_counts = {}
        hobby_counts = {}
        habit_counts = {}

        # 5. Lặp qua từng bạn trực tiếp
        for friend in friends_set:
            # Lấy bạn của bạn (bạn của bạn)
            foafs = self.graph.neighbors(friend)
            foafs_set = set()
            for foaf in foafs:
                foafs_set.add(foaf)

            # 6. Với từng bạn của bạn (foaf)
            for foaf in foafs_set:
                # Bỏ qua user và bạn trực tiếp
                if foaf == user_id:
                    continue
                if foaf in friends_set:
                    continue

                # Đếm số bạn chung
                if foaf in mutual_counts:
                    mutual_counts[foaf] += 1
                else:
                    mutual_counts[foaf] = 1

                # Tính số sở thích chung
                if foaf in self.students:
                    foaf_hobbies = self.students[foaf].hobbies
                else:
                    foaf_hobbies = set()

                common_hobbies = set()
                for hobby in user.hobbies:
                    if hobby in foaf_hobbies:
                        common_hobbies.add(hobby)

                hobby_counts[foaf] = len(common_hobbies)

                # Tính số thói quen chung
                if foaf in self.students:
                    foaf_habits = self.students[foaf].habits
                else:
                    foaf_habits = set()

                common_habits = set()
                for habit in user.habits:
                    if habit in foaf_habits:
                        common_habits.add(habit)

                habit_counts[foaf] = len(common_habits)

        # 7. Tính điểm tổng và tìm max_score để chuẩn hóa
        scores = {}
        max_score = 0
        for uid in mutual_counts:
            score = (w_mutual * mutual_counts[uid] +
                     w_hobby * hobby_counts.get(uid, 0) +
                     w_habit * habit_counts.get(uid, 0))
            scores[uid] = score

            if score > max_score:
                max_score = score

        # 8. Chuẩn hóa điểm về thang 0-10
        recommendations = []
        for uid in scores:
            if max_score > 0:
                normalized_score = (scores[uid] / max_score) * 10
            else:
                normalized_score = 0
            recommendations.append((uid, normalized_score))

        # 9. Sắp xếp thủ công (selection sort) theo điểm giảm dần
        n = len(recommendations)
        for i in range(n - 1):
            max_idx = i
            for j in range(i + 1, n):
                if recommendations[j][1] > recommendations[max_idx][1]:
                    max_idx = j
            if max_idx != i:
                recommendations[i], recommendations[max_idx] = recommendations[max_idx], recommendations[i]

        # 10. Trả về tối đa max_results kết quả
        return recommendations[:max_results]
