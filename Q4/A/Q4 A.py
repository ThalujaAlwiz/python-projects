option=input("Enter 1 convert from Celsius to Fahrenheit or 2 for convert from Fahrenheit to Celsius[1/2] ")

if option=="1":
    Celsius=float(input("Enter Celsius value "))
    Fahrenheit= (Celsius * 1.8) + 32
    print("Fahrenheit value is ",Fahrenheit)
elif option=="2":
    Fahrenheit=float(input("Enter Fahrenheit value "))
    Celsius = (Fahrenheit - 32) / 1.8
    print("Celsius value is ",Celsius)
else:
    print("invalid option entered")
