meal_cost=int(input("Enter r the cost of the meal "))
print()
print(" satisfaction level: 1 = Totally satisfied, 2 = Satisfied, 3 = Dissatisfied")
option=input("Enter you satisfaction level ")
print()
if option=="1":
    tip=meal_cost*20/100
    print("tip ",tip)
elif option=="2":
    tip=meal_cost*15/100
    print("tip ",tip)
elif option=="3":
    tip=meal_cost*10/100
    print("tip ",tip)
else:
    print("Invalid option")




      
