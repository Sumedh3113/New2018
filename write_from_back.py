"""
MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'
"""
def master_yoda(text):
    q = text.split()
    z = -1
    p =''
    for i in q:
        p = p +" "+ q[z]
        z = z-1
        
    return p

x = master_yoda('I am home')
print(x)