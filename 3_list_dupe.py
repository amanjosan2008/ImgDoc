x=[1,2,3,4,5,6,2,4]
y=['a','b','c','d','e','f','g','h']
z=[]

for i in range(len(x)):
    for j in range(i+1, len(x)):
        if x[i] == x[j]:
            z.append(x[i])
print(z)

for i in range(len(z)):
    for j in range(len(x)):
        if z[i] == x[j]:
                print(y[j])
