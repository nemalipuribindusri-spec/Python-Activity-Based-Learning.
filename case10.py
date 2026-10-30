marks = [
    [80, 75, 90],
    [60, 70, 65],
    [95, 90, 92]
]

student_number = 1

for row in marks:
    total = row[0] + row[1] + row[2]
    average = total / 3

    print("Student", student_number)
    print("Total =", total)
    print("Average =", average)

    student_number = student_number + 1