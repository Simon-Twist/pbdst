#Simon Twist
#10369980
#A calculator with a choice of functions.

import string

def menu():															#Help screen
	print "\n   Functions menu:" 
	print "    1 Factorial"
	print "    2 Addition"
	print "    3 Subtraction"
	print "    4 Multiplication"
	print "    5 Division"
	print "    6 Exponent"
	print "    7 Square"
	print "    8 Cube"
	print "    9 Square Root"
	print "   10 Cube Root"
	print "   11 Mode"
	print "   12 Root"
	print "   13 Maximum"
	print "   14 Prime Checker"
	
	print   "\n   To continue press Enter."
	raw_input("   To exit press Ctrl and Z together, followed by Enter. ") #^Z will cause an exception which will be caught by the try-catch around main().
	print ""														#Enter (with any input or none) will send the user back to the input field they were at.

def check(prompt,charList,max):                                     #Checks characters against a list of valid characters. Checks length.
	valid = False
	
	while valid == False:                                           #Get new input until valid.
		try:
			string = raw_input(prompt)
		except EOFError:											#^Z will call menu().
			menu()
			continue												#If menu() does not cause a 2nd exception then user is continuing. Ask for input again.
		
		valid = True
		
		for ch in string:                                           #Loop through each character entered.
			chValid = False
			
			for ascii in charList:                                  #Loop through the list of valid characters.
				if ascii == ord(ch):                                #If list entry does not match character, check next list entry. If matches, character valid.
					chValid = True									#Set chValid so "Invalid" will not print.
					break											#If match found, don't check character against the rest of the list.
			
			if chValid == False:                                    #If the flag is still False the character was not on the list.
				print "           Invalid character."
				valid = False										#Stay in input loop.
				break												#Only print "Invalid character" once then get new input.
		
		if max<len(string):											#If too long, stay in input loop.
			print "               %d characters or fewer please." % (max)
			valid = False
	
	return string													#return valid string

#1 Factorial
def factorial(a):
	if a<0:
		return "infinite"
	if a==0:
		return 1
	else:
		return a*factorial(a-1)

def fact(a):
	return map(factorial,a)

#2 Addition
def add(a,b):
	return map(lambda x,y: x+y, a,b)
	
#3 Subtraction
def subtract(a,b):
	return map(lambda x,y: x-y, a,b)

#4 Multiplication
def multiply(a,b):
	return map(lambda x,y: x*y, a,b)

#5 Division
def div(a,b):
	if b!=0:
		return float(a)/b
	return "Cannot divide by 0"
	
def divide(a,b):
	return map(div, a,b)

#6 a to the power of b
def expo(a,b):
	if not (a==0 and b<1):
		return a**b
	return "Error"

def exponent(a,b):
	return map(expo, a,b)
	
#7 a squared
def square(a):
#	return map(lambda x: x*x, a)
	return [x*x for x in a]

#8 a cubed
def cube(a):
	return map(lambda x: x*x*x, a)

#9 square-root of a
def sqRoo(a):
	if a<0:
		return "a complex number"
	return a**(1/2.0)

def sqrRoot(a):
	return map(sqRoo, a)

#10 cube-root of a
def cuRoo(a):
	if a<0:													#the two minus signs are because
		return -(-a)**(1/3.0)								#Python will not normally accept
	return a**(1/3.0)										#negative numbers with exponents <1

def cubeRoot(a):
	return map(cuRoo, a)

#11 the modal elements in a list
def mode(a):
	counts=[]
	
	i=0
	while i<len(a):
		counts.append(0)
		
		k=0
		while k<len(a):
			if a[i]==a[k]:
				counts[i]=counts[i]+1
			k=k+1
		
		i=i+1
	
	modelist=[]
		
	m=0
	while m<len(a):
		if counts[m]==max(counts):
			modelist.append(a[m])
		m=m+1
	
	norepeats=[]
	norepeats.append(modelist[0])
	n=0
	while n<len(modelist):
		onlist=False
		
		g=0
		while g<len(norepeats):
			if modelist[n]==norepeats[g]:
				onlist=True
			g=g+1
		if onlist==False:
			norepeats.append(modelist[n])
		n=n+1
	
	return norepeats

#12	general roots
def rt(a,b):
	if a==0 and (1/b)<1:
		return "Error"
	if a<0 and b%2==1:								
		return -(-a)**(1.0/b)
	if a<0 and b%2==0:
		return "a complex number"
	if b>=1:
		return a**(1.0/b)
	return "Error"

def root(a,b):
	return map(rt, a,b)
	
#13 maximum
def larger(a,b):
	if a<b:
		return b
	else:
		return a

def maximum(a):
	return reduce(larger,a)

#14 prime numbers
def prime(a):
	for x in range(a):
		if x!=0 and x!=1 and (a/float(x))%1==0:
			return False
	return True
	
def primelist(a):
	return filter(prime, a)

def main():
	#valid input
	digits=[48,49,50,51,52,53,54,55,56,57]									#0 1 2 3 4 5 6 7 8 9
	decimals=[48,49,50,51,52,53,54,55,56,57,46]								#0 1 2 3 4 5 6 7 8 9 .

	print "\n   This is a calculator with 12 functions."					#intro
	print "   For the menu press Ctrl and Z together, followed by Enter."	#list of functions available

	#keep looping until user quits	
	while True:
		#which function?
		rawchoice=check("\n   Please enter the number of the function you would like to use: ",digits,10000)
		choice=int(rawchoice)

		#1 Factorial
		if choice==1:
			a=input("\n   Please enter the list: ")
			print "  ",a,"factorial is",fact(a)

		#2 Addition
		elif choice==2:
			a=input("\n   Please enter the 1st list: ")
			b=input("   Please enter the 2nd list: ")
			print "  ",a,"plus",b,"is",add(a,b)

		#3 Subtraction
		elif choice==3:
			a=input("\n   Please enter the 1st list: ")
			b=input("   Please enter the 2nd list: ")
			print "  ",a,"minus",b,"is",subtract(a,b)

		#4 Multiplication
		elif choice==4:
			a=input("\n   Please enter the 1st list: ")
			b=input("   Please enter the 2nd list: ")
			print "  ",a,"multiplied by",b,"is",multiply(a,b)

		#5 Division
		elif choice==5:
			a=input("\n   Please enter the 1st list: ")
			b=input("   Please enter the 2nd list: ")
			print "  ",a,"divided by",b,"gives",divide(a,b)

		#6 a to the power of b
		elif choice==6:
			a=input("\n   Please enter the 1st list: ")
			b=input("   Please enter the 2nd list: ")
			print "  ",a,"to the power of",b,"is",exponent(a,b)

		#7 squared
		elif choice==7:
			a=input("\n   Please enter the list: ")
			print "  ",a,"squared is",square(a)

		#8 cubed
		elif choice==8:
			a=input("\n   Please enter the list: ")
			print "  ",a,"cubed is",cube(a)

		#9 square-root
		elif choice==9:
			a=input("\n   Please enter the list: ")
			print "   The square-root of",a,"is",sqrRoot(a)

		#10 cube-root
		elif choice==10:
			a=input("\n   Please enter the list: ")
			print "   The cube-root of",a,"is",cubeRoot(a)

		#11 mode
		elif choice==11:
			a=input("\n   Please enter a list in square brackets, e.g. [1,2,2,3]: ")
			m=mode(a)
			s=""
			c=0
			while c<len(m):
				s=s+str(m[c])+" "									#convert to a string for display
				c=c+1
			if len(m)==1:
				print "   The mode of",a,"is",s
			elif 1<len(m):
				print "   The modes of",a,"are the following: ",s

		#12 general roots
		elif choice==12:
			a=input("\n   Please enter the 1st list: ")
			b=input("   Please enter the 2nd list: ")
			print "   The",b,"root of ",a,"is",root(a,b)

		#13 maximum
		elif choice==13:
			a=input("\n   Please enter the list: ")
			print "   The maximum value of",a,"is",maximum(a)

		#14 prime
		elif choice==14:
			a=input("\n   Please enter the list to be checked: ")
			print "   These are the prime numbers in the list:",primelist(a)

try:
	main()
except:																#^Z on the Menu screen must be caught here.
	print "\n   The programme has exited."							#If it is caught in the menu() function the programme will not exit.