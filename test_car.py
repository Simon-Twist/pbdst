
import unittest

from car import *
from DBSCarRental import *

# test the car functionality
class TestCar(unittest.TestCase):

	#1
	def test_car_mileage(self):
		self.car = Car()
		self.assertEqual(0, self.car.getMileage())
		self.car.move(15)
		self.assertEqual(15, self.car.getMileage())
		self.car.setMileage(45)
		self.assertEqual(45, self.car.getMileage())

	#2
	def test_car_make(self):
		self.car = Car()
		self.assertEqual('', self.car.getMake())
		self.car.setMake('Ferrari')
		self.assertEqual('Ferrari', self.car.getMake())

	#3
	def test_car_colour(self):
		self.car = Car()
		self.assertEqual('', self.car.getColour())
		self.car.paint('red')
		self.assertEqual('red', self.car.getColour())
		self.car.setColour('yellow')
		self.assertEqual('yellow', self.car.getColour())

	#4
	def test_car_engine_size(self):
		self.car = Car()
		self.assertEqual('', self.car.engineSize)
		self.car.engineSize = '2.0tdi'
		self.assertEqual('2.0tdi', self.car.engineSize)

	#5
	def test_electric_car_fuel_cells(self):
		electric_car = ElectricCar()
		self.assertEqual(1, electric_car.getNumberFuelCells())
		electric_car.setNumberFuelCells(4)
		self.assertEqual(4, electric_car.getNumberFuelCells())
		
	#6
	def test_hybrid_car_fuel_cells(self):
		car = HybridCar()
		self.assertEqual(1, car.getNumberFuelCells())
		car.setNumberFuelCells(4)
		self.assertEqual(4, car.getNumberFuelCells())		

	#7
	def test_petrol_car_cylinders(self):
		car = PetrolCar()
		self.assertEqual(1, car.getNumberCylinders())
		car.setNumberCylinders(4)
		self.assertEqual(4, car.getNumberCylinders())
		
	#8
	def test_diesel_car_cyliders(self):
		car = DieselCar()
		self.assertEqual(1, car.getNumberCylinders())
		car.setNumberCylinders(4)
		self.assertEqual(4, car.getNumberCylinders())
		
	#9
	def test_type(self):
		cars=[PetrolCar(),DieselCar(),HybridCar(),ElectricCar()]
		correct=["p","d","h","e"]
		self.assertEqual(correct,[cars[0].getType(),cars[1].getType(),cars[2].getType(),cars[3].getType()])

	#10
	def test_RentalCo_create_stock(self):
		Co=RentalCo()
		Co.create_current_stock(1,2,3,4)
		self.assertEqual(1,len(Co.petrol_cars))
		self.assertEqual(2,len(Co.diesel_cars))
		self.assertEqual(3,len(Co.hybrid_cars))
		self.assertEqual(4,len(Co.electric_cars))

	#11
	def test_RentalCo_free(self):
		Co=RentalCo()
		Co.create_current_stock(2,3,4,5)
		self.assertEqual([2,3,4,5],Co.free())

	#12
	def test_RentalCo_rent(self):
		Co=RentalCo()
		Co.create_current_stock(3,4,5,6)
		Co.rent(Co.petrol_cars,"Simon",2)
		self.assertEqual("Simon",Co.petrol_cars[0].renter)
		self.assertEqual("Simon",Co.petrol_cars[1].renter)

	#13 Tester must return p1 and p3 when prompted
	def test_RentalCo_Return(self):
		Co=RentalCo()
		Co.create_current_stock(3,4,5,6)
		Co.rent(Co.petrol_cars,"Simon",3)
		Co.Return("Simon","p",Co.petrol_cars,2)
		self.assertEqual("",Co.petrol_cars[0].renter)
		self.assertEqual("Simon",Co.petrol_cars[1].renter)
		self.assertEqual("",Co.petrol_cars[2].renter)

	#14
	def test_stock_count(self):
		Co=RentalCo()
		Co.create_current_stock(3,4,5,6)
		Co.stock_count()
		
	#15 Tester may return p1-p5
	def test_inventory(self):
		Co=RentalCo()
		Co.create_current_stock(5,5,5,5)
		Co.rent(Co.petrol_cars,"Mr. P",5)
		Co.rent(Co.diesel_cars,"Ms. D",5)
		Co.rent(Co.hybrid_cars,"Ms. H",5)
		Co.rent(Co.electric_cars,"Mr. E",5)
		Co.Return("Mr. P","p",Co.petrol_cars,1)
		Co.inventory()
		
	#16 Tester enters Tester > y > d > 2 > n
	def test_process_rental(self):
		Co=RentalCo()
		Co.create_current_stock(4,3,2,1)
		Co.process_rental()
		self.assertEqual("Tester",Co.diesel_cars[0].renter)
		self.assertEqual("Tester",Co.diesel_cars[1].renter)
		self.assertEqual("",Co.diesel_cars[2].renter)
		
#In total, tester enters e.g. n > n > n > n > p1 > p3 > p2 > Tester > y > d > 2

if __name__ == '__main__':
	unittest.main()
