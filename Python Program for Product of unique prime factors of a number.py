# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 17:18:37 2022

@author: ugly
"""

# Python program to find sum of given
# series.

def productPrimeFactors(n):
	product = 1
	
	for i in range(5, n+1):
		if (n % i == 0):
			isPrime = 1
			
			for j in range(3, int(i/2 + 1)):
				if (i % j == 0):
					isPrime = 0
					break
				
			# condition if \'i\' is Prime number
			# as well as factor of num
			if (isPrime):
				product = product * i
				
	return product
	
	
	
# main()
n = 99

print (productPrimeFactors(n))

# Contributed by _omg
