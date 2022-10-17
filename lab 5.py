def printJobScheduling(arr, t):
	n = len(arr)
	for i in range(n):
		for j in range(n - 1 - i):
			if arr[j][2] < arr[j + 1][2]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

	result = [False] * t   # To keep track of free time slots
 
	job = ['-1'] * t   # To store result (Sequence of jobs)

	for i in range(len(arr)):  # Iterate through all given jobs

		# last possible slot)
		for j in range(min(t - 1, arr[i][1] - 1), -1, -1):

			# Free slot found
			if result[j] is False:
				result[j] = True
				job[j] = arr[i][0]
				break
	print(job)  # print the sequence


# Driver's Code
if __name__ == '__main__':
	arr = [['a', 2, 100], # Job of array
			['b', 1, 19],
			['c', 2, 27],
			['d', 1, 25],
			['e', 3, 15]]
	print("Following is maximum profit sequence of jobs")
	printJobScheduling(arr, 3) #function call

