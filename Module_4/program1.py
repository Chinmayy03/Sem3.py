num=[1,2,3,2,4,1,3,3,2]
frequency={}
for i in num:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1        
print(frequency)