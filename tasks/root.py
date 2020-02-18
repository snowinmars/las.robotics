import math

number = None

while number is None:
    answer = input("Enter a number: ")
    number = float(answer)

if number < 0:
    raise Exception(f'{number} is less them zero, cant calculate a real square')

print(math.sqrt(number))
