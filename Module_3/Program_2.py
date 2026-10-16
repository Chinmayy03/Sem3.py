print("        A grading system for students     ")
n = int(input("Pls enter how many subjects u have:"))
t = 0
for i in range(0,n):
    q  = int(input("Marks:"))
    t += q
avg = t/n

if int(avg) >= 90:
    print("Grade A")
elif int(avg) >= 70:
    print("Grade B")
elif int(avg) >= 60:
    print("Grade C")
else:
    print("Fail")
print("Total:",q)
print("Average:",avg)