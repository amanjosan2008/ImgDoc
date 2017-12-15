
y = [1,4,2,3,20,49,0,49,50,56,51,5,70,97,99,98,100]
z = []
for i in range(len(y)):
    for j in range(i+1, len(y)):
            if (abs(y[i] - y[j])) < 8:
                print(y[i])
                z.append(y[i])

for i in range(len(z)):
    try:
        y.remove(z[i])
    except:
        pass

print(y)
