x = int(input("Enter x: "))

while x % 2 == 0 or x % 5 == 0:
    x = int(input("Please enter another value of x: "))

print(f"Input x: {x}")

def check_beautiful_number(number):
    number_str = str(number)
    check = all(digit == number_str[0] for digit in number_str)
    return check

def smallest_beautiful_number(x):
    initial = x
    digit = x
    length = 0
    while digit % x != 0 or not check_beautiful_number(digit):
        digit += 1
        if len(str(digit)) > length:
            length += 1
            digit = initial * length
    return digit

beautiful_number = smallest_beautiful_number(x)

print(f"The smallest beautiful number divisible by {x} is {beautiful_number}")