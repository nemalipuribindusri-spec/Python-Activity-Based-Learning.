def attendance_calculator(attended, total):
    if total <= 0 or attended < 0 or attended > total:
        print("Invalid data")
    else:
        percentage = attended * 100 / total
        extra = 0

        while percentage < 75:
            attended += 1
            total += 1
            extra += 1
            percentage = attended * 100 / total

        print("Attendance =", percentage, "%")
        print("Additional classes needed =", extra)

    print()


# 5 Test Cases
attendance_calculator(80, 100)
attendance_calculator(60, 100)
attendance_calculator(30, 50)
attendance_calculator(0, 40)
attendance_calculator(110, 100)