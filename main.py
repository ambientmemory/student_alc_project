import csv, statistics
debug = False
data = []
no_of_features = 0

def load_data():
	with open('student/student-mat.csv', 'r') as csvfile:
		data_reader = csv.reader(csvfile, delimiter=';', quotechar='"')
		next(data_reader)
		for row in data_reader:
			no_of_features = len(row)
			# print(row[23])
			# data.extend(row[1])
			# data.append(row)
			print(row[3])
			#print(numerize(row[3]))
#end of load_data

def clean_data():
	if debug:
		print(len(data))
		print(data[:][0]==data[0][:])
		print([sub_list[0] for sub_list in data])
		print(data[23])
	#for i in range(0, no_of_features):
	#school_name = [sub_list[0] for sub_list in data]

def numerize(str_list):
	set_vals = set(str_list)
	print(set_vals)
	# set_vals contains the A or B options
	dict_map = {}
	numerized_list = []
	for set_elem in set_vals:
		for i in range(0,len(set_vals)-1):
			dict_map = dict(set_elem=i)
	print(dict_map)
	for element in str_list:
		numerized_list = dict_map[element]
	print(numerized_list)
	return numerized_list

def normalize(numeric_list):
	mean = statistics.mean(numeric_list)
	std_dev = statistics.stdev(numeric_list)
	#Using sample statistics here
	numeric_list[:] = [((x-mean)/std_dev) for x in numeric_list]
	return numeric_list



load_data()
clean_data()