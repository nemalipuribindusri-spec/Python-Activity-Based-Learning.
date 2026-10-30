def product_bill(price, quantity):
    if price <= 0 or quantity <= 0:
        print("Invalid input")
    else:
        subtotal = price * quantity

        if subtotal >= 1000:
            discount = subtotal * 0.10
        else:
            discount = 0

        final = subtotal - discount

        print("Subtotal =", subtotal)
        print("Discount =", discount)
        print("Final bill =", final)

    print()


# Test Case 1
product_bill(100, 5)

# Test Case 2
product_bill(200, 5)

# Test Case 3
product_bill(50, 10)

# Test Case 4
product_bill(-100, 5)

# Test Case 5
product_bill(250, 4)