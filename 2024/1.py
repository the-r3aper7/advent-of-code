from collections import Counter

testcases = []
with open("./1_test.txt") as file:
    for line in file.readlines():
        testcases.append(line.strip("\n"))

def solve_part_1(left_arr, right_arr):
    answer = 0
    for k, v in enumerate(left_arr):
        answer += abs(v - right_arr[k])
    return answer

left_arr = []
right_arr = []

for testcase in testcases:
    x, y = testcase.split("  ")
    left_arr.append(int(x))
    right_arr.append(int(y))
left_arr.sort()
right_arr.sort()
print(solve_part_1(left_arr, right_arr)) # 2166959

def solve_part_2(left_arr, right_arr):
    count_left = Counter(left_arr)
    count_right = Counter(right_arr)
    similarity = 0
    for k, v in count_left.items():
        similarity += (k * v * count_right[k])
    return similarity

print(solve_part_2(left_arr, right_arr)) # 23741109