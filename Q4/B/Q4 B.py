num1=int(input("Enter number 1 "))
num2=int(input("Enter number 2 "))
print()
print("Integer 1\tOperator\tInteger 2\tExpected Rusult")
print(num1,"\t|\t","+\t|\t",num2,"\t|\t",num1+num2)
print(num1,"\t|\t","-\t|\t",num2,"\t|\t",num1-num2)
print(num1,"\t|\t","*\t|\t",num2,"\t|\t",num1*num2)
try:
    print(num1,"\t|\t","/\t|\t",num2,"\t|\t",num1/num2)
except ZeroDivisionError :
    print(num1,"\t|\t","/\t|\t",num2,"\t|\t","Error")
