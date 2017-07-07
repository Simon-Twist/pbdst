#Simon Twist
#10369980
#7 July 2017

#Define Car
class Car(object):
#Implement the car object.
	
	def __init__(self):
		self.__colour = ""
		self.__make = ""
		self.__mileage = 0
		self.engineSize = ""
		self.renter = ""
		self.reg=""

	def getColour(self):
		return self.__colour

	def getMake(self):
		return self.__make

	def getMileage(self):
		return self.__mileage

	def setColour(self, colour):
		self.__colour = colour

	def setMake(self, make):
		self.__make = make

	def setMileage(self, mileage):
		self.__mileage = mileage

	def paint(self, colour):
		self.__colour = colour
		return self.__colour

	def move(self, distance):
		self.__mileage = self.__mileage + distance
		return self.__mileage

#1 Petrol inherits from Car
class PetrolCar(Car):

	def __init__(self):
		Car.__init__(self)
		self.__numberCylinders = 1
		self.__type = "p"

	def getType(self):
		return self.__type
		
	def setType(self,letter):
		self.__type = letter
		
	def getAvail(self):
		return self.__available
		
	def setAvail(self,TrueFalse):
		self.__available = TrueFalse

	def getNumberCylinders(self):
		return self.__numberCylinders

	def setNumberCylinders(self, value):
		self.__numberCylinders = value

#2 Diesel inherits from Car
class DieselCar(Car):

	def __init__(self):
		Car.__init__(self)
		self.__numberCylinders = 1
		self.__type = "d"

	def getType(self):
		return self.__type
		
	def getNumberCylinders(self):
		return self.__numberCylinders

	def setNumberCylinders(self, value):
		self.__numberCylinders = value

#3 Electric inherits from Car
class ElectricCar(Car):
	
	def __init__(self):
		Car.__init__(self)
		self.__numberFuelCells = 1
		self.__type = "e"

	def getType(self):
		return self.__type

	def getNumberFuelCells(self):
		return self.__numberFuelCells

	def setNumberFuelCells(self, value):
		self.__numberFuelCells = value

#4 Hybrid inherits from PetrolCar
class HybridCar(PetrolCar):
	
	def __init__(self):
		PetrolCar.__init__(self)
		self.__numberFuelCells = 1
		self.setType("h")

	def getNumberFuelCells(self):
		return self.__numberFuelCells

	def setNumberFuelCells(self, value):
		self.__numberFuelCells = value