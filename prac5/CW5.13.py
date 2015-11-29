marks = input().split()
for i in range(10):
    marks[i] = int(marks[i])
sum = marks[9]
number_of_marks = 1
for i in range(9):
    if marks[i] != 2 or marks[i+1] == 2:
        sum += marks[i]
        number_of_marks += 1
average = sum / number_of_marks
print(int(average // 1))
