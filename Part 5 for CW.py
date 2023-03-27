print("--PROGRAM--START","\n")

#Create Variables

P = 0     #P = Pass
D = 0     #D = Defer
F = 0     #F = Fail
PR = 0    #PR = Progress
T = 0     #T = Trailer
E = 0     #E = Exclude
R = 0     #R = Retriever
OL = 0    #OL = Outcome of the List

#Function 1
#To Get the Program Outcome      

def Output_of_program():
    global PR,T,R,E                                                          
    if P == 120 and D == 0 and F == 0:                                          #Progression for "Progress"
        print("Progress",P,D,F)
        PR += 1

    elif P == 100 and D <= 20 and F <=20:                                       #Progression for "Progress(Module Trailer)"
        print("Progress (Module Trailer)",P,D,F)
        T += 1

    elif P <= 40 and D <= 40 and F >= 80 and F <=120:                             #Progression for "Exclude"  
        print("Exclude",P,D,F)
        E += 1

    else:                                            
        print("Do not progress - Module Retriever",P,D,F)                             #Progression for "Do Not Progress- Module Retriever" 
        R += 1
                                                                       

#Function 2
#create the Horizontal Histogram

def HH():                 #HH = Horizontal_Histogram
    print('\n')
    print('-'*100)
    print('Horizontal Histogram','\n')
    print('Progress ',PR,':', '*'*PR)                    #Outcome of "Progress"
    print('Trailer  ',T,':', '*'*T)                      #Outcome of "Trailer"
    print('Retreiver',R,':', '*'*R)                      #Outcome of "Retriver"
    print('Exclude  ',E,':', '*'*E,'\n')                 #Outcome of "Exclude"
    print((PR + T + E + R ), 'Outcomes in Total')        #To get total number of student records
    print('-'*100)


#Body of The Program
#Create The Progression Outcomes List

OL = [[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]]


for i in range (0,10):                
    P = OL[i][0]       # 0 index for Pass 
    D = OL[i][1]       # 1 index for Defer 
    F = OL[i][2]       # 2 index for Fail 

    #Calling Function 1
    Output_of_program()

#Calling Function 2    
HH()

#End of the Program

print("\n","--PROGRAM--END")
