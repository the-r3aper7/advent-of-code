testcases = []
with open("./1_test.txt") as file:
    for line in file.readlines():
        testcases.append(line.strip("\n"))

def get_number(string) -> int:
    i = 0
    j = len(string) - 1
    left_digit = ""
    right_digit = ""
    while len(left_digit) != 1 or len(right_digit) != 1:
        if ord(string[i]) in range(48, 57 + 1):
            left_digit = string[i]
        else:
            i += 1
        if ord(string[j]) in range(48, 57 + 1):
            right_digit = string[j]
        else:
            j -= 1
    return int(left_digit + right_digit)

answer = 0
for word in testcases:
    answer += get_number(word)
print(answer)