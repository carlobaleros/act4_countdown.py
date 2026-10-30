#Baleros Carlo D.
#Baet 2102
count = 0
total = 0.0

while True:
    price = float(input("Price (0 to stop): "))
    if price == 0:
        break
    total += price
    count += 1

print(f"Items: {count}  Total: {total:.2f}")

if count > 0:
    average = total / count
    print(f"Average: {average:.2f}")
else:
    print("Average: 0.00")
