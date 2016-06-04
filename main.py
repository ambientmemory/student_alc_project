import csv, statistics, numpy as np
import pandas

debug = False
no_of_features = 0

def clean_data():
	data = pandas.read_csv('student/student-mat.csv', sep=';')
	# making school information redundant
	data.ix[:, 0] = 0.1
	numerization_indices = {'1', '3', '4', '5', '8', '9', '10', '11', '15', '16', '17', '18', '19', '20', '21', '22'}
	normalization_indices = {'2', '29', '30', '31', '32'}
	#running numerization loop here
	for num_idx in numerization_indices:
		data.ix[:,int(num_idx)] = numerize(data.ix[:,int(num_idx)])
	#running normalization loop here
	for norm_idx in normalization_indices:
		data.ix[:, int(norm_idx)] = normalize(data.ix[:,int(norm_idx)])
	if debug:
		print(data)

def numerize(str_list):
	set_vals = set(str_list)
	if debug:
		print(set_vals)
	# set_vals contains the 'A' or 'B' options
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