"""
return reverse of binary
and then convert the reverse value to integer
"""
import sys

def rev_bin(num):
     x = "{0:b}".format(num)
     return list(reversed(x))
     
value = int(sys.stdin.readline())     
     
result = rev_bin(value)

y = ''.join(result)

z = int(y,2)# type cast to integer

sys.stdout.write(str(z))