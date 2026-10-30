balance = 1000

transactions = [
    ("D", 500),
    ("W", 200),
    ("W", 2000),
    ("D", 300),
    ("W", 100)
]

for kind, amount in transactions:
    if amount <= 0:
        print("Invalid amount")
    elif kind == "D":
        balance = balance + amount
    elif kind == "W":
        if amount <= balance:
            balance = balance - amount
        else:
            print("Insufficient balance")
    else:
        print("Invalid type")

print("Final balance = Rs.", balance)