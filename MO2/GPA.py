#Logan Metcalfe
#GPA calculator
#This program will take a name and GPA input and calculate whether or not it made the deans list, or honor roll.
deansList = float(3.5) #initiallized the values for these two variables.
honors = float(3.25)
name =  str(input("Enter the name of the student: ")) #First input, can use zzz. ZZZ will not close the loop.
while name != "zzz": #While loop
    try: #Basic input validation
        gpa = float(input("input the GPA for the student: ")) #Second input
        if gpa >= deansList: #Determines the first condition, which is greater than 3.5
            print(name + " qualifies for Deans List.") #output
        elif gpa < deansList and gpa > honors: #Determines second condition, greater than 3.25, but less than 3.5
            print(name + " qualified for Honors.") #output
        else: #Anything else did not qualify 
            print (name + " did not qualify for Deans List or Honors.")
        name =  str(input("Enter the name of the student: ")) #loop restarts
    except:
        print("invalid Input.") #outputs when an invalid input is sent for the GPA (not a number)