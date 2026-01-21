import random
import string

def generate_password(length, complexity):
    if complexity == "1":  # Easy
        characters = string.ascii_lowercase
    elif complexity == "2":  # Medium
        characters = string.ascii_letters + string.digits
    elif complexity == "3":  # Strong
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("=== Password Generator ===")
print("Select Password Complexity:")
print("1. Easy (Lowercase letters)")
print("2. Medium (Letters + Numbers)")
print("3. Strong (Letters + Numbers + Symbols)")

try:
    choice = input("Enter your choice (1/2/3): ")
    length = int(input("Enter desired password length: "))

    if length < 4:
        print("Password length must be at least 4 characters.")
    else:
        password = generate_password(length, choice)
        if password:
            print("Generated Password:", password)
        else:
            print("Invalid complexity choice.")

except ValueError:
    print("Please enter valid numeric input.")
