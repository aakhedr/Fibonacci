def fib_recurse(n):
	"""
	n = Integer
	Recursively calculate fibonacchi of n
	"""
	if (n <= 1):
		return n
	else:
		return fib_recurse(n - 1) + fib_recurse(n - 2)

def fib_table(n):
	"""
	n = Integer
	Faster fibonacci of n 
	O(n)
	"""
	table = [0, 1]
	first = 0
	second = 1

	for i in range(n - 1):
		third = first + second
		table.append(third)

		first = second
		second = third
		
	return table[-1]

import time

def stressTest(n):
	"""
	Output of both above functions should be identical.
	Difference is comuting times where fib_table should be faster.
	"""
	t1 = time.time()
	slow_fib = fib_recurse(n)
	t2 = time.time()
	diff1 = t2 - t1
	
	t3 = time.time()
	fast_fib = fib_table(n)
	t4 = time.time()
	diff2 = t4 - t3
	
	if slow_fib == fast_fib:
		print("Fib of", str(n), "is equal by both functions:", fast_fib)
	else:
		print("Fib of", str(n), "is NOT equal by both functions.", "'slow_fib'=", slow_fib, "'fast_fib'=", fast_fib)
		break
	
	if diff1 > diff2:
		print("'fib_table' faster than 'fib_table'")
	elif diff1 < diff2:
		print("'fib_recurse' faster than 'fib_table'")
		break
	else:
		print("both functions were computed in equal times")
		break

