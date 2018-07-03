import unittest
import os
#from ctypes import *

while(True):
	os.system("g++ trial.cpp -o sumedh.exe")
	result = os.system("sumedh.exe")
	#os.system("5")

	print("Result",result)	
	class TestCalc(unittest.TestCase):
		def test_add(self):	
		#result = self.add(10,5)
			self.assertEqual(result, 12)

	name = input("Enter your name\n")
	#next =1;		

	with open("Sumedh.xls","a") as s:
		s.write(name)
		s.write("\t")
		s.write(str(result))
		s.write("\n")
	#s = open('Sumedh.xls','a')
	#s.append(name)
	
	inp = input("Do you want to Exit?(y/n)\n")
	if(inp == 'y'):
		break
		s.close()
	"""else:
		next = next + 1
		s.seek(next)
"""

"""g = open('Sumedh.txt')
p = g.read()
print(p)s.
"""
	
		
if 	__name__ == '__main__':
	unittest.main()