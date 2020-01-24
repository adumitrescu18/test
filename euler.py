import time
def isPrime(n):
	boolean = True
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			boolean = False
			break
	return boolean
# print(isPrime(3175))




def largestPrime(n):
	i = 2
	max1 = 0
	start = time.time()
	while i * i < n:

		if n%i == 0 and isPrime(i) == True and i > max1:
			max1 = i
		i+= 1
	end = time.time()
	return(max1, end-start)
# print(largestPrime(600851475143))


def divBy20(n):
	boolean = True
	for i in range(11, 20):

		if n%i != 0:
			boolean = False
			break
	return boolean


def smallestNumber():
	i = 2520
	start = time.time()
	while True:
		if divBy20(i):
			end = time.time()
			return (i, end-start)
		i += 2520

print(smallestNumber())
