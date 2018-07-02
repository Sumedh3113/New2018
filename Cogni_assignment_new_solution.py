d = [3,1,2,5,7,5,7,2,5,4] 
dire = {}
rev = {}
value = []
ans = []
last = []
for i in d:
    #print(dire[i])
    dire[i] = 0
for i in d:
    dire[i] = dire[i] + 1
for a,b in dire.items():
    while b: 
        last.append(a)
        b = b - 1

for a,b in dire.items():
    #rev[b] = a
    value.append([a,b])
    #rev[b] = a
    
maxim = 0
freq1 = []
for k in range(len(value)):
    
    for i in range(len(value)):
        if maxim < value[i][1]:
            if value[i][1] > 1:
                maxim = value[i][1]
            else:
                freq1.append(value[i][0])


    for i in range(len(value)):
        
        if maxim > 1:
            if maxim == value[i][1]:
                while value[i][1] > 0:
                    ans.append(value[i][0])
                    value[i][1] = value[i][1] -1
                maxim = value[i][1]
            
            
            #ans.append(freq)
            
            

print(freq1)

#c = max(value)
print(ans)



'''for a,b in dire.items():
    #s = max(b)
    key.append(a)
    value.append(b)
    #sorted(dire)        
for x in range(len(key)):
    while value[x] > 0:
        last.append(key[x])
        value[x] = value[x]-1
'''      
            
#print(last)
print(maxim)
