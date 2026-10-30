def hospital_bill(consultation, tests, treatment):
    if consultation < 0 or tests < 0 or treatment < 0:
        print("Invalid charges")
    else:
        total = consultation + tests + treatment

        if total >= 5000:
            discount = total * 0.10
        else:
            discount = 0

        final = total - discount

        print("Subtotal =", total)
        print("Concession =", discount)
        print("Final bill =", final)
        print()


# Test Case 1
hospital_bill(500, 1000, 2000)

# Test Case 2
hospital_bill(1000, 2000, 3000)

# Test Case 3
hospital_bill(200, 300, 400)

# Test Case 4
hospital_bill(1500, 2500, 1000)

# Test Case 5
hospital_bill(-100, 500, 1000)