print("Enter the marks scored by the students")
Written = int(input("Written test = "))
lab = int(input("Lab exams = "))
Assignments = int(input("Assignments = "))
Grade = (Written*70)/100 + (lab*20)/100 + (Assignments*10)/100 
print("Grade of the student is = ",str(Grade))