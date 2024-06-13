#Logan Metcalfe
#GPA calculator
#This program will take a name and GPA input and calculate whether or not it made the deans list, or honor roll.
deansList = float(3.5)
honors = float(3.25)
name =  str(input("Enter the name of the student: "))
while name != "zzz":
    try:
        gpa = float(input("input the GPA for the student: "))
        if gpa >= deansList:
            print(name + " qualifies for Deans List.")
        elif gpa < deansList and gpa > honors:
            print(name + " qualified for Honors.")
        else:
            print (name + " did not qualify for Deans List or Honors.")
        name =  str(input("Enter the name of the student: "))
    except:
        print("invalid Input.")