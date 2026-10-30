def attendance_calculator(attended, total):
    if total <= 0 or attended < 0 or attended > total:
        print("Invalid data")
    else:
        percentage = attended * 100 / total
        extra = 0

        while percentage < 75:
            attended = attended + 1
            total = total + 1
            extra = extra + 1
            percentage = attended * 100 / total

        print("Attendance =", percentage, "%")
        print("Additional classes needed =", extra)

    print()


# Test Case 1
attendance_calculator(80, 100)

# Test Case 2
attendance_calculator(60, 100)

# Test Case 3
attendance_calculator(30, 50)

# Test Case 4
attendance_calculator(0, 40)

# Test Case 5
attendance_calculator(110, 100)