from collections import defaultdict

input_list = [[0, 30], [5, 10], [5, 10], [15, 20]]

actions_points = defaultdict(int)

for item in input_list:
    actions_points[item[0]] += 1
    actions_points[item[1]] -= 1

actions_points = sorted(actions_points.items())

max_num_of_conference_rooms = 0
num_of_conferece_rooms = 0

for action_point in actions_points:
    num_of_conferece_rooms += action_point[1]
    max_num_of_conference_rooms = max(
        num_of_conferece_rooms, max_num_of_conference_rooms
    )

print(max_num_of_conference_rooms)
