x=int(input("enter the no.of subjects: "))
y=0
for i in range(x):
    z=int(input("enter the marks: "))
    y += z
avg = y / x
print("total marks:",y)


if int(avg)>=90:
    print("A grade")
elif int(avg)>=80:
    print("B grade")
elif int(avg)>=70:
    print("C grade")
elif int(avg)>=60:
    print("D grade")
else:
    print("F grade")
print(f"average marks: {avg}")