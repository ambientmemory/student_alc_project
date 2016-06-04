import csv, statistics, numpy as np
import pandas, random

debug = False
global train_x
global train_y
global test_x
global test_y

def clean_data():
	data = pandas.read_csv('student/student-mat.csv', sep=';')
	# making school information redundant
	data.ix[:, 0] = 0.1
	numerization_indices = {1, 3, 4, 5, 8, 9, 10, 11, 15, 16, 17, 18, 19, 20, 21, 22}
	normalization_indices = {2, 29, 30, 31, 32}
	#running numerization loop here
	for num_idx in numerization_indices:
		data.ix[:,num_idx] = numerize(data.ix[:,num_idx])
	#running normalization loop here
	for norm_idx in normalization_indices:
		data.ix[:, norm_idx] = normalize(data.ix[:,norm_idx])
	# Partition function splits the data up into test and training
	# TODO: Cross validation?
	#train_x, train_y, test_x, test_y = partition_data(data)
	partition_data(data)
	'''
	if debug:
		#print(data)
		print('Training x is: \n', train_x)
		print('Training y is: \n', train_y)
		print('Testing x is: \n', test_x)
		print('Testing y is: \n', test_y)
	'''

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

def partition_data(data):
	global train_x
	global train_y
	global test_x
	global test_y
	'''
	Partitions the data into x and y, testing and training
	:param data: cleaned pandas dataframe
	:return: train_x, train_y, test_x, test_y
	'''
	# TODO: Cross-validation?
	no_of_rows = len(data.index)
	# randomly choose a partition size here
	train_partition_size = random.randint((no_of_rows-1)/2, no_of_rows-2)
	col_name = input('Please enter the column number of the feature you want to predict: ')
	col_no = data.columns.get_loc(col_name)
	# Training lot
	train_x = data.ix[:train_partition_size,:]
	train_x = train_x.drop(col_name, 1)
	train_y = train_x.ix[:, col_no]
		#Testing lot
	test_x = data.ix[train_partition_size+1:,:]
	test_x = test_x.drop(col_name, 1)
	test_y = test_x.ix[:, col_no]
	#if debug:
	#	print('Partitioning training set at row no:', train_partition_size)
	#	print(train_x)
	#	print(test_x)
	#   print(train_y)
	#   print(test_y)
	#return train_x, train_y, test_x, test_y

def print_wtf():
	print('Training x is: \n', train_x)
	print('Training y is: \n', train_y)
	print('Testing x is: \n', test_x)
	print('Testing y is: \n', test_y)

clean_data()