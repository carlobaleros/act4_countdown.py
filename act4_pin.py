#Baleros Carlo D.
#BAET 2102
CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3
attempts = 0

while attempts < MAX_ATTEMPTS:
    user_pin = input("PIN: ")
    if user_pin == CORRECT_PIN:
        print("Access granted")
        break
    attempts += 1

if attempts == MAX_ATTEMPTS:
    print("Card blocked")
