x = ['a',5,'b',7,'c',9]
y = {}
print (y)
for i in range(0,len(x),2):
    y[x[i]] = x[i+1]
print(y)