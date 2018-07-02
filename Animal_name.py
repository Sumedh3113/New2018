"""
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False
"""

def animal_crackers(text):
    p = text.split()
    #print(p[0][0])
    return p[0][0] == p[1][0]
