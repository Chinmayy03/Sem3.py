print("program 1")
num = [1,2,3,2,4,1,3,3,2]
freq = {}
for i in num:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)