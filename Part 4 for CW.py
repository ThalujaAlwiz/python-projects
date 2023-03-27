print("--PROGRAM--START","\n")

#Create Variables

P = 0     #P = Pass
D = 0     #D = Defer
F = 0     #F = Fail
PR = 0    #PR = Progress
T = 0     #T = Trailer
E = 0     #E = Exclude
VH = 0    #VH = Vertical Histogram
V = 0     #V = Variable
R = 0     #R = Retriever
VL = 0    #VL = Vertical List
PT = 0    #PT = Progression Type
PRO = 0   #PRO = Progression


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
    global PR,T,R,E
    
    Tot = True              #Tot = Total
    
    if P + D + F == 120:                                                            #The user input values must equal to 120 for the Program

        if P == 120 and D == 0 and F == 0:                                          #Progression for "Progress"
            print("Progress")
            PR += 1

        elif P == 100 and D <= 20 and F <=20:                                       #Progression for "Progress(Module Trailer)"
            print("Progress (Module Trailer)")
            T += 1

        elif P <= 40 and D <= 40 and F >= 80 and F <=120:                             #Progression for "Exclude"  
            print("Exclude")
            E += 1

        else:                                            
            print("Do not progress - Module Retriever")                             #Progression for "Do Not Progress- Module Retriever" 
            R += 1
            
    elif P + D + F > 120:                                                           #If the user input values are more than 120
        
        print("--- Total Inccorect ---","\n")
        Tot = False
    else:                                                
        print("---Total Inccorect --- ","\n")
        Tot = False   
        
    return Tot                                                                      #Return to Function 1

#Function 3
#creating Vertical Histogram

def VH():
    print("\n")
    print("-"*100)

#Creat a List for Vertical
#Create a 2D list.
#List have main 4 indexces

    VL=[[],[],[],[]]            #VL = Vertical List
                                #Create a list variable helps to Collect data to printing part
    
    print("Vertical Histogram\n")
    print("Progress","|"," Trailer","|"," Retriever","|"," Exclude")

#Find max count between (PR,T,R,E)
    PT = max(PR,T,R,E)                       # max == sub list's indexses count

#Makeing a loop using max 
#Creating first 0 index in VL
    
    for a in range(PT):        
        if PR > a:                                              #Find if progress value less than a or not. This part run when if True
            PRO = 1                                             #Assign Progression to 1
        else:                                                   #This part run when if False
            PRO = 0                                             #Assign Progression to 0
    
        VL[0].append(PRO)                                       # Add 1's and 0's to 0th index

#Creating 1 st 1 index in VL   
    for a in range(PT):        
        if T > a:                           
            PRO = 1                         
        else:                               
            PRO = 0                     
        VL[1].append(PRO)                   

#Creating 1 st 2 index in VL
    for a in range(PT):        
        if R > a:                       
            PRO = 1                         
        else:                               
            PRO = 0                         
        VL[2].append(PRO)               

#Creating 1 st 3 index in VL
    for a in range(PT):        
        if E > a:                           
            PRO = 1                         
        else:                               
            PRO = 0                              
        VL[3].append(PRO)                        
    
        
    
    for i in range(len(VL[0])):   #This loop use for print part
        
        #Get length of VL list
        #Creating a loop using length
        #Print * multiplying by sub list's values
        
        print(" "*5+"*"*VL[0][i]+" ",end="\t")  #Print 1 st sub list's indexes, delete last newline charecter
        print(" "*10+"*"*VL[1][i]+" ",end="\t") #Print 2 nd                   ", "                           "
        print(" "*8+"*"*VL[2][i]+" ",end="\t")  #Print 3 rd                   ", "                           "
        print(" "*5+"*"*VL[3][i])               #Print 4 th sub list's indexes.


    print("\n")
    print(PR+T+R+E,"outcomes in total.") #To get the total of students records   
    print("-"*100)

#Making loop to input multiple records

V = True                                
while V:
    Tlist()                             #Calling Function 1
    print("\n","--- Would you like to Enter another set of Data? ---")
    while True:
        try:
            YM = input("Enter 'y' for YES or 'q' to Quit and view Results: " )
            if YM.lower() == "q":                       #Set V to False if the 'q' string value found. It not be continue the while loop anymore and  it runs the rest of Histogram and End
                V = False
                break
            elif YM.lower() != "y":                     #If user isn't input a letter from "y" and "q", Display the incorrect message and continue the loop
                print("User Input is incorrect","\n")
            else:                                       #If user input "y", break the loop
                print("\n")                             #Then the user can input a different record
                print("-"*100)
                break
        except:                                         
            print("User Input is incorrect","\n")

#Calling Function 3
VH()

#End of the Program

print("\n","--PROGRAM--END")

