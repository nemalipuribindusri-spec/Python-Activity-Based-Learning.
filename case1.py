def electricity_bill(units):
    if units < 0:
        return "Invalid units"
    elif units <= 100:
        charge = units * 2
    elif units <= 200:
        charge = 100 * 2 + (units - 100) * 3
    else:
        charge = 100 * 2 + 100 * 3 + (units - 200) * 5

    bill = charge + 50
    return bill


# 5 Test Cases
print("Test Case 1:", electricity_bill(50))
print("Test Case 2:", electricity_bill(100))
print("Test Case 3:", electricity_bill(150))
print("Test Case 4:", electricity_bill(250))
print("Test Case 5:", electricity_bill(-10))