# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.

# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):

	# Check base case
	if high >= low:

		mid = (high + low) // 2

		# If element is present at the middle itself
		if arr[mid] == x:
			return 1

		# If element is smaller than mid, then it can only
		# be present in left subarray
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)

		# Else the element can only be present in right subarray
		else:
			return binary_search(arr, mid + 1, high, x)

	else:
		# Element is not present in the array
		return 0


n , q = list(map(int, input().split()))
array = list(map(int, input().split()))
answers = []

for i in range(q):
    line = input().split()
    key = int(line[1])
    answers.append(binary_search(array,0,n-1, key))


#print("these are n and q: ",n,q)

#print("this is input array: ",array)

#print("these are answers array: ",answers)

for element in answers:
    print(element)
    