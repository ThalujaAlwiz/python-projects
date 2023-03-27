mark=int(input("Enter marks "))

if mark>0 and 100>mark:
    if mark >= 70:
        print("Exceptional result!")
    elif mark >= 40:
        print("Satisfactory result!")
    else:
        print("You have failed.")
else:
    print("exam mark is invalid ")
