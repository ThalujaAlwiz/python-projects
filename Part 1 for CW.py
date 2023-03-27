print("--PROGRAM--START","\n")

#Create Variables

P = 0     #P = Pass
D = 0     #D = Defer
F = 0     #F = Fail

#Function
#Main Process of the Program

def Output_of_program():
    if P == 120 and D == 0 and F == 0:                  # Progression for "Progress"
        print(" Progress ")
    elif P == 100 and D <= 20 and F <=20:               # Progression for "Progress(Module Trailer)"
        print(" Progress (Module Trailer) ")
    elif P <= 40 and D <= 40 and F >= 80 and F <=120:     # Progression for "Exclude"
        print(" Exclude ")
    else:
        print(" Do Not Progress - Module Retriever ")     # Progression for "Do Not Progress- Module Retriever"

#Input Process of the Program
        
#Input Integers Only

P = int(input(" Please Enter Your Credits at Pass : "))
D = int(input(" Please Enter Your Credits at Defer: "))
F = int(input(" Please Enter Your Credits at Fail : "))

#Calling The Function
Output_of_program()

#End of the Program

print("\n","--PROGRAM--END")

