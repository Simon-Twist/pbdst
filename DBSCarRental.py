#Simon Twist
#10369980
#7 July 2017

from car import *	

class RentalCo(object):

#Set up lists of cars.
	def __init__(self):
		self.petrol_cars = []
		self.diesel_cars = []
		self.hybrid_cars = []
		self.electric_cars = []

#Grow each list to the appropriate number of cars.
	def create_current_stock(self,p,d,h,e):
		for i in range(p):
			self.petrol_cars.append(PetrolCar())
			self.petrol_cars[i].reg="%s%d" % (self.petrol_cars[i].getType(),i+1)
		for i in range(d):
			self.diesel_cars.append(DieselCar())
			self.diesel_cars[i].reg="%s%d" % (self.diesel_cars[i].getType(),i+1)
		for i in range(h):
			self.hybrid_cars.append(HybridCar())
			self.hybrid_cars[i].reg="%s%d" % (self.hybrid_cars[i].getType(),i+1)
		for i in range(e):
			self.electric_cars.append(ElectricCar())
			self.electric_cars[i].reg="%s%d" % (self.electric_cars[i].getType(),i+1)

#Return the number of unrented cars of each type.
	def free(self):
		p=0
		d=0
		h=0
		e=0
		for car in self.petrol_cars:
			if car.renter=="":
				p=p+1
		for car in self.diesel_cars:
			if car.renter=="":
				d=d+1
		for car in self.hybrid_cars:
			if car.renter=="":
				h=h+1
		for car in self.electric_cars:
			if car.renter=="":
				e=e+1
		return [p,d,h,e]

#Print the number of unrented cars of each type.
	def stock_count(self):
		list=self.free()
		print "\n                 Petrol cars in stock:",list[0]
		print "                 Diesel cars in stock:",list[1]
		print "                 Hybrid cars in stock:",list[2]
		print "               Electric cars in stock:",list[3]
		
#Check there are enough cars available.
#If so, assign the desired number of cars to the renter.
	def rent(self, car_list, renter, amount):
		free=0
		for car in car_list:
			if car.renter=="":
				free=free+1
		if free < amount:
			print "\n             Not enough cars in stock."
			return
		else:
			count = 0
			for car in car_list:
				if car.renter=="" and count < amount:
					car.renter=renter
					count = count + 1

#Get customer name
#Find out if renting or returning
#Pass rent() or Return() the appropriate list of cars to adjust
	def process_rental(self):
		renter = raw_input("\n                     Renter's name/ID: ")
		answer = raw_input("     Would you like to rent a car y/n? ")
		if answer == "y":
			list=self.free()
			#If all cars are rented out:
			if list[0]==0 and list[1]==0 and list[2]==0 and list[3]==0:
				print "\n   Sorry nothing to rent, please try again."
			else:
				answer = raw_input("     What type would you like p/d/h/e? ")
				amount = int(raw_input("              How many would you like? "))
				if answer == "p":
					self.rent(self.petrol_cars, renter, amount)
				elif answer == "d":
					self.rent(self.diesel_cars, renter, amount)
				elif answer == "h":
					self.rent(self.hybrid_cars, renter, amount)
				elif answer == "e":
					self.rent(self.electric_cars, renter, amount)
		else:
			answer = raw_input("   Would you like to return a car y/n? ")
			if answer == "y":
				type = raw_input("  What type are you returning p/d/h/e? ")
				amount = int(raw_input("    How many would you like to return? "))
				if type == "p":
					self.Return(renter, type, self.petrol_cars, amount)
				elif type == "d":
					self.Return(renter, type, self.diesel_cars, amount)
				elif type == "h":
					self.Return(renter, type, self.hybrid_cars, amount)
				elif type == "e":
					self.Return(renter, type, self.electric_cars, amount)
		self.inventory()

#If the customer's name is on the car they wish to return, remove the name.
#If not, inform the user.
	def Return(self, returner, type, car_list, amount):
		list=self.free()
		if type == "p":
			index=0
		elif type == "d":
			index=1
		elif type == "h":
			index=2
		elif type == "e":
			index=3

		if amount<=len(car_list)-list[index]:
			for i in range(amount):
				incar=raw_input("          Which car is being returned? ")
				for car in car_list:
					if car.reg==incar:
						if returner==car.renter:
							car.renter=""
						else:
							print "\n         ",returner,"did not rent this car."
		else:
			print "\n       Cannot return more than rented."

#Print all cars and any renters assigned.
	def inventory(self):
		print "\n     Car Renter"
		for i in self.petrol_cars:
			print "   %5s %s" %(i.reg,i.renter)
		for i in self.diesel_cars:
			print "   %5s %s" %(i.reg,i.renter)
		for i in self.hybrid_cars:
			print "   %5s %s" %(i.reg,i.renter)
		for i in self.electric_cars:
			print "   %5s %s" %(i.reg,i.renter)
	
def main():
	p,d,h,e=20,8,8,4
	DBSCarRental = RentalCo()
	DBSCarRental.create_current_stock(p,d,h,e)
	DBSCarRental.inventory()
	proceed = "y"
	while proceed == "y":
		DBSCarRental.process_rental()
		proceed = raw_input("\n                         Continue y/n? ")

main()