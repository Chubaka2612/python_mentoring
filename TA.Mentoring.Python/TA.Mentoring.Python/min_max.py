def show_min_max(list):
	print ("min: " + str(find_min(list)))
	print ("max: " + str(find_max(list)))

def find_min(list):
	min = None
	for item in list:
		number = get_int(item)
		if not bool(number):
			continue
		elif not bool(min):
			min = number
		elif number < min:
			min = number
	return min

def find_max(list):
	max = None
	for item in list:
		number = get_int(item)
		if not bool(number):
			continue
		elif not bool(max):
			max = number
		elif number > max:
			max = number
	return max

def get_int(item):
	try:
		if item is not None:
			return int(item)
	except ValueError:
		try:
			return int(float(item))
		except ValueError:
			return None