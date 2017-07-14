import unittest
from listcalculator import factorial, fact, add, subtract, multiply, div, divide, expo, exponent, square, cube, sqRoo, sqrRoot, cuRoo, cubeRoot, mode, rt, root, larger, maximum, prime, primelist

#test all calculator functions
class TestCalculator(unittest.TestCase):
	#1
	def testFact(self):
		self.assertEqual(["infinite",1,1,120,720,3628800],fact([-3,0,1,5,6,10]))

	#2
	def testAdd(self):
		self.assertEqual([2,-1,1,15,31,-7],add([-3,0,1,5,6,-3],[5,-1,0,10,25,-4]))
		
	#3
	def testSubtract(self):
		self.assertEqual([-8,1,1,-5,-19,1],subtract([-3,0,1,5,6,-3],[5,-1,0,10,25,-4]))
		
	#4
	def testMultiply(self):
		self.assertEqual([-15,0,0,50,150,12],multiply([-3,0,1,5,6,-3],[5,-1,0,10,25,-4]))
		
	#5
	def testDivide(self):
		self.assertEqual([-0.6,0,"Cannot divide by 0",0.5,0.24],divide([-3,0,1,5,6],[5,-1,0,10,25]))
		
	#6
	def testExponent(self):
		self.assertEqual([-243,"Error",1,9765625,244140625],exponent([-3,0,1,5,25],[5,-1,0,10,6]))		
		
	#7
	def testSquare(self):
		self.assertEqual([9,0,1,25,625,1],square([-3,0,1,5,25,-1]))

	#8
	def testCube(self):
		self.assertEqual([-27,0,1,125,15625,-1],cube([-3,0,1,5,25,-1]))
	
	#9
	def testSqrRoot(self):
		self.assertEqual(["a complex number",0,1,5,"a complex number"],sqrRoot([-3,0,1,25,-1]))
		
	#10
	def testCubeRoot(self):
		self.assertEqual(map(round,[-1.4422496,0,1,2.9240177,-1],[7,7,7,7,7]),map(round,cubeRoot([-3,0,1,25,-1]),[7,7,7,7,7]))
		
	#11
	def testMode(self):
		self.assertEqual([4],mode([1,2,3,4,4,4,5,6,7,7,8]))
		self.assertEqual([1,2,3],mode([1,2,3]))
		self.assertEqual([8],mode([8,4,5,6,3,8,7]))
		self.assertEqual([6],mode([2,5,6,36,7,6,7,8.2,3,4.4,5,6]))
		self.assertEqual([1.2],mode([1.1,1.2,1.4,1.2,1.5,1.2,1.4,1.3]))
		self.assertEqual(["a"],mode(["a","b","c","a","d"]))
		self.assertEqual(["a",2],mode(["a",1,2,2,2,"a",1,"a"]))
		
	#12
	def testRoot(self):
		self.assertEqual([-1.2457309396155174,"Error","Error",3,1.452495661406287,"a complex number"],root([-3,0,1,81,6,-3],[5,-1,0,4,4.8,2]))
		
	#13
	def testMax(self):
		self.assertEqual(100,maximum([1,2,54,56,12,-1,-1414,100,23,-43.33,.23,0]))

	#14
	def testprimelist(self):
		self.assertEqual([2,23],primelist([1,2,54,56,12,-1,-1414,100,23,-43.33,.23,0]))
		self.assertEqual([1901,1907,1913,1931,1933,1949,1951,1973,1979,1987,1993,1997,1999],primelist(range(1900,2000)))
		self.assertEqual([1000003,1000033,1000037,1000039,1000081,1000099],primelist(range(1000000,1000100)))


if __name__=="__main__":
	unittest.main()