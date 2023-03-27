print("--PROGRAM--START","\n")

#Create Variables

P = 0     #P = Pass
D = 0     #D = Defer
F = 0     #F = Fail

#Create List Range
LR = [0,20,40,60,80,100,120]        #LR = List Range 

#Function 1
#Input Process of the Program
#Program Only takes Integer values only
#Program Only takes List Range Values Only

def Tlist():
    global P, D, F

    while True:                                                            
        while True:
            try:
                P = int(input("Please Enter Your Credits At Pass : "))             #Input the Value for Pass as an Integer
                if P not in LR:                                                    #Checking the Pass input value is not in the given Range
                    print("---Out of Range---","\n")            
                else:
                    break                                                          #If the given input value is in the given List Range then go to the next Process
            except:
                print("---Integer Required---","\n")                               #If the Given Pass input value is not an Integer 

        while True:
            try:
                D = int(input("Please Enter Your Credits At Defer: "))              #Input the Value for Defer as an Integer
                if D not in LR:                                                     # Checking the Defer input value is not in the given Range
                    print("---Out of Range---","\n")            
                else:
                    break                                                           #If the given input value is in the given List Range then go to the next Process
            except:
                print("---Integer Required---","\n")                                #If the Given Defer input value is not an Integer      
        while True:
            try:
                F = int(input("Please Enter Your Credits At Fail : "))              #Input the Value for Fail as an Integer
                if F not in LR:                                                     #Checking the Fail input value is not in the given Range
                    print("---Out of Range---","\n")
                else:
                    break                                                           #If the given input value is in the given List Range then go to the next Process
            except:
                print("---Integer Required---","\n")                                #If the Given Fail input value is not an Integer

        Tot = Output_of_program()                                                   #Calling Function 2
        if Tot:                                                                     #If total is True program ends and If Total is False program continues to Function 1 for get new values
            break

#Function 2
#Main Process of the Program
#Progress to check the total of user input values equal to 120         

def Output_of_program():

    Tot = True              #Tot = Total
    
    if P + D + F == 120:                                                            #The user input values must equal to 120 for the Program

        if P == 120 and D == 0 and F == 0:                                          #Progression for "Progress"
            print("Progress")

        elif P == 100 and D <= 20 and F <=20:                                       #Progression for "Progress(Module Trailer)"
            print("Progress (Module Trailer)")

        elif P <= 40 and D <= 40 and F >= 80 and F <=120:                           #Progression for "Exclude"  
            print("Exclude")

        else:                                            
            print("Do not progress - Module Retriever")                             #Progression for "Do Not Progress- Module Retriever" 

    elif P + D + F > 120:                                                           #If the user input values are more than 120
        
        print("--- Total Inccorect ---","\n")
        Tot = False
    else:                                                
        print("---Total Inccorect --- ","\n")
        Tot = False   
        
    return Tot                                                                      #Return to Function 1

#Calling Function 1
Tlist()


#End of the Program

print("\n","--PROGRAM--END")
