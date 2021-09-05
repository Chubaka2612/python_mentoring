def get_multiple_of(limit, divs):
	result = []
	for i in range(1, limit):
		if any(i % div == 0 for div in divs):
			result.append(i)
	return result
			
def sum_of(numbers):
	total_sum = 0
	for number in numbers:
		total_sum = total_sum + number
	return total_sum

def show_sum_multiple_of(limit = 10000, divs = (3, 5)):
	sum = sum_of(get_multiple_of(limit, divs))
	print("Total sum for numbers in range 1,", limit, "multiple to", divs, "is", sum)