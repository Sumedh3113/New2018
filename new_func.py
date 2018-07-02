""" 
refer the image for the question --> func_question
que:-

Pass a string and return every even letter in upper case and odd letter in lower case
"""
new_name = input("Eneter the name\n")


def myfunc(name):
    s = name
    p = ''
    index = 0
    for _ in s:
        if index%2 == 0:
            p = p + s[index].lower()
        else:
            p = p + s[index].upper()
        index = index +1    
    
    return p
    
s = myfunc(new_name)
print(s)
"""
#Solution by github

def myfunc(x):
    out = []
    for i in range(len(x)):
        if i%2==0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)
	
"""