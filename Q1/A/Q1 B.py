n = input('Give me a number over 100: ')
try:
    if int(n) <= 100:
        print(n, 'is not over 100')
except ValueError:
    print("Requires a valid integer!")


