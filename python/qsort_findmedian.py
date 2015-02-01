from array import *
from random import *

# Program to find the Kth largest number in unordered list.
# Uses Quicksort partioning. Also implemented Quicksort, Insertion sort.

def findKth(a, k):
	assert 0 <= k and k < len(a)
	return findMedianSub(a, 0, len(a) - 1, k)

def findMedian(a):
	return findMedianSub(a, 0, len(a) - 1, len(a) / 2)

def findMedianSub(a, start, end, k):
	pivotIndex = partition(a, start, end, randint(start, end))
	# Now, everything above pI > a[pi]
	if pivotIndex == k:
		return a[k]
	else:
		if pivotIndex > k:	# Discard everything above!
			return findMedianSub(a, start, pivotIndex-1, k)
		else:					# Discard everything below!
			return findMedianSub(a, pivotIndex+1, end, k)

# Taken from http://en.literateprograms.org/Quicksort_(Python,_arrays)
def partition(a, start, end, pivotIndex):
	low = start
	high = end - 1  # After we remove pivot it will be one smaller
	pivotValue = a[pivotIndex]
	a[pivotIndex] = a[end]	# remove pivot from array
	while True:
		while low <= high and a[low] < pivotValue:
			low = low + 1
		while low <= high and a[high] >= pivotValue:
			high = high - 1
		if low > high:
			break
		a[low], a[high] = a[high], a[low]
	# insert pivot into final position and return final position
	a[end] = a[low]
	a[low] = pivotValue
	# print "Partition(a, %d, %d, %d) = %s" % (start, end, pivotIndex, str(low))
	return low

def qsortRange(a, start, end):
	if end - start + 1 < 32:
		insertionSort(a, start, end)
	else:
		pivotPoint = randint(start, end)
		pivotIndex = partition(a, start, end, pivotPoint)
		# print "partition(a, %d, %d, %d) = %s" % (start, end, pivotPoint, str(pivotIndex))
		qsortRange(a, start, pivotIndex - 1)
		qsortRange(a, pivotIndex + 1, end)
	return a

def qsort(a):
	return qsortRange(a, 0, len(a) - 1)

def insertionSort(a, start, end):
	# TODO: Understand this
	for i in xrange(start, end + 1):
		# Insert a[i] into the sorted sublist
		v = a[i]
		for j in reversed(xrange(0, i)):
			if a[j] <= v:
				a[j + 1] = v
				break
			a[j + 1] = a[j]
		else:
			a[0] = v
	return a

def randarray(typecode, numElements, minValue, maxValue):
	a = array(typecode)	# Or just a = list() !!!!
	for i in xrange(0, numElements):
		a.append(randint(minValue, maxValue))
	return a

def checkArraySorted(a):
	for i in xrange(1, len(a) - 1):
		if a[i] < a[i-1]:
			return False
	return True

if __name__ == '__main__':
	# TODO: partition the array using quicksort, eliminate the ends.
	a = randarray('i', 111, 1, 200)
	print a
	print "Median = %d" % findMedian(a)
	print "Kth(10th) = %d" % findKth(a, 10)
	qsort(a)
	print a
	print "Qsort Median = %d" % a[len(a)/2]
	print "Qsort Kth = %d" % a[10]
	# print qsort(a)
	# if checkArraySorted(qsort(randarray('i', 10000, 0, 999999999))):
	# 	print "Test passed"
	# else:
	# 	print "Test failed"
