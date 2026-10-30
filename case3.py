def salary_calculation(basic, allowance, deduction):
    if basic < 0 or allowance < 0 or deduction < 0:
        print("Invalid values")
    else:
        gross = basic + allowance

        if deduction > gross:
            print("Invalid deduction")
        else:
            net = gross - deduction
            print("Gross salary =", gross)
            print("Net salary =", net)

    print()


# Test Case 1
salary_calculation(20000, 5000, 2000)

# Test Case 2
salary_calculation(30000, 5000, 10000)

# Test Case 3
salary_calculation(15000, 2000, 17000)

# Test Case 4
salary_calculation(-5000, 1000, 500)

# Test Case 5
salary_calculation(25000, 3000, 0)