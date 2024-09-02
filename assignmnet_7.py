name = input("Enter your name: ")
n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))
n3 = int(input("Enter your third number: "))

print(f"\nHello, {name}! Let's explore your favorite numbers:")

list_num = [n1, n2, n3]

for i in list_num:
    if i % 2 == 0:
        print(f"The number {i} is even.")
    else:
        print(f"The number {i} is odd.")

for i in list_num:
    print(f"The number {i} and its square is ({i}, {i**2})")

sum = n1 + n2 + n3
print(f"\nAmazing! The sum of your favorite numbers is {sum}")

if sum > 1 and all(sum % i != 0 for i in range(2, int(sum**0.5) + 1)):
    print(f"Wow, {sum} is a prime number!")
else:
    print(f"{sum} is not a prime number.")
