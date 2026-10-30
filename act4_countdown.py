#Baleros Carlo D.
#Baet 2102
# Read a whole number n. Keep asking while n is not positive.
n = int(input("Enter n: "))
while n <= 0:
    n = int(input("Enter n: "))

# Count down from n to 1 on one line and finish with "Liftoff!"
while n > 0:
    print(n, end=" ")
    n -= 1

print("Liftoff!")
