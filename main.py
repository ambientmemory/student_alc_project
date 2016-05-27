import csv, statistics, numpy as np
import pandas

debug = False
no_of_features = 0

def clean_data():
	data = pandas.read_csv('student/student-mat.csv', sep=';')
	# making school information redundant
	data.ix[:, 0] = 0.1
	'''
	for i in range(0,395):
		#binarizing gender: Male = 0, Female = 1
		if data.ix[i,1]=='M':
			data.ix[i,1] = 0
		else:
			data.ix[i,1] = 1
		#binarising address: Rural = 0, Urban = 1
		if data.ix[i, 3] == 'R':
			data.ix[i, 3] = 0
		else:
			data.ix[i, 3] = 1
		#binarizing famsize: Less than 3 = 0, Greater than 3 = 1
		if data.ix[i, 4] == 'LE3':
			data.ix[i, 4] = 0
		else:
			data.ix[i, 4] = 1
	'''
	# calling numerize
	data.ix[:,1] = numerize(data.ix[:,1])
	print(data)
	if debug:
		print(data)

def numerize(str_list):
	set_vals = set(str_list)
	if debug:
		print(set_vals)
	# set_vals contains the A or B options
	dict_map = {}
	numerized_list = []
	#building the index map here
	i = 0
	for set_elem in set_vals:
		dict_map.update({set_elem:i})
		i = i+1
	if debug:
		print(dict_map)

	for text_thing in str_list:
		numerized_list.append(dict_map.get(text_thing))
	if debug:
		print(numerized_list)
	return numerized_list

def normalize(numeric_list):
	mean = statistics.mean(numeric_list)
	std_dev = statistics.stdev(numeric_list)
	#Using sample statistics here
	numeric_list[:] = [((x-mean)/std_dev) for x in numeric_list]
	return numeric_list



clean_data()