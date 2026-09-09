name= input("Enter your name: ")#taking user input for his/her name
usn= input("Enter your usn: ")    #taking user input for his/her usn

print(f"My name is {name}")       #displaying the name and usn of the user
print(f"My usn is {usn}")

marks1= int(input("Enter marks for subject 1: "))
marks2= int(input("Enter marks for subject 2: "))  
marks3= int(input("Enter marks for subject 3: "))   #taking user input for marks of subject 1,2 and 3

total= marks1 + marks2 + marks3
print(f"Total marks is {total}")   #displaying the total marks of the user

average= total/3                    
print(f"Average marks is {average:0.2f}")    #displaying the average marks of the user
