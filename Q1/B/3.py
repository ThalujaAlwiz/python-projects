Age=input("Enter age?")
try:
    if int(Age)>=18:
        print("can vote")
except ValueError:
    print("Requires age in  a valid integer!")

