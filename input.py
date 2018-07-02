name = input("Enter your name\n")

dict ={'Sumedh': 25 , 'Chandu' : 24 , 'Pritam' : 23}

print("Age:", dict[name])

index = int(input("Enter A number between 1-10\n"))

list = ['Tall','Short', 'Dark', 'Smart', 'Evil']

if index < 5 and index > 1:
	print (list[index])
else:
	print(list[index-5])