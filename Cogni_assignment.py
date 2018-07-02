"""enter a list [3,1,2,5,7,5,7,2,5]
op should be [5,5,5,7,7,2,2,1,3]
if freq then desc order if not then ascend order
"""

d = [3,1,2,5,7,5,7,2,5] 
dire = {}
value = []
key = []
last = []
common = []
x = 0
e = 0
maxi =0
listi = []
for i in range(0,9):
    for j in d:
        if i ==j:
            x = x+1
            last.append(j)
    key.append(x)
    x = 0
    
'''for p in range(2,9):
    for o in range(2,9):
        if o == key[o]:
        common.append(o)

for o in key:
    if o not in common:
        common.append(o)
        
'''   

maxi = max(key)
#x = maxi
for i in range(1,9):
    for j in range(1,9):
        
        if maxi == key[j]:
            for _ in range(maxi):
                value.append(j)

    maxi = maxi-1 
    


print(value)
    