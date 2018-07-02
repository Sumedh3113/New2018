"""
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald
Note: 'macdonald'.capitalize() returns 'Macdonald'
"""
def old_macdonald(name):
    s = ''
    for i in range(len(name)):
        if i == 0:
            s =s + name[0].upper()
        elif i == 3:
            s =s + name[3].upper()
        else:
            s =s + name[i]
    return s
	

result = old_macdonald('macdonald')

print(result)