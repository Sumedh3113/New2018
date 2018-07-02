"""
Return even numbers from passed integers
"""

def myfunc(*args):
    list1 =[]
    list1 = [item for item in args if item % 2 ==0]
    return list1
        
value = myfunc(2,3,6,4,8,5)

print(value)


"""
Given Solution by Udemy:-

def myfunc(*args):
    out = []
    for num in args:
        if num%2==0:
            out.append(num)
    return out
"""