def check_performance(marks):
    print("Assessment marks:", marks)

    change = marks[2] - marks[0]
    print("Change =", change)

    if change > 0:
        print("Performance improved")
    elif change < 0:
        print("Performance declined")
    else:
        print("Performance unchanged")

    print()


# 5 Test Cases
check_performance([60, 70, 85])
check_performance([90, 80, 70])
check_performance([75, 75, 75])
check_performance([40, 60, 80])
check_performance([85, 70, 50])