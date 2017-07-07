import unittest

from car import *

# test the car functionality
class TestCar(unittest.TestCase):

	def test_car_mileage(self):
		self.car = Car()
		self.assertEqual(0, self.car.getMileage())
		self.car.move(15)
		self.assertEqual(15, self.car.getMileage())
		self.car.setMileage(45)
		self.assertEqual(45, self.car.getMileage())

	def test_car_make(self):
		self.car = Car()
		self.assertEqual('', self.car.getMake())
		self.car.setMake('Ferrari')
		self.assertEqual('Ferrari', self.car.getMake())

	def test_car_colour(self):
		self.car = Car()
		self.assertEqual('', self.car.getColour())
		self.car.paint('red')
		self.assertEqual('red', self.car.getColour())
		self.car.setColour('yellow')
		self.assertEqual('yellow', self.car.getColour())

	def test_car_engine_size(self):
		self.car = Car()
		self.assertEqual('', self.car.engineSize)
		self.car.engineSize = '2.0tdi'
		self.assertEqual('2.0tdi', self.car.engineSize)

	def test_electric_car_fuel_cells(self):
		electric_car = ElectricCar()
		self.assertEqual(1, electric_car.getNumberFuelCells())
		electric_car.setNumberFuelCells(4)
		self.assertEqual(4, electric_car.getNumberFuelCells())

if __name__ == '__main__':
	unittest.main()
