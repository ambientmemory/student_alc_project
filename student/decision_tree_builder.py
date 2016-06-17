'''
Used to build thee decision tree classifier
'''

import pandas as pd

def decision_tree_builder(train_x, train_y):
	'''
	Applies Hunt's Algorithm to a variant of ID3 decision tree
	:param train_x:
	:param train_y:
	:return:
	'''

	#finds the increasing information gain per column
	entropy_vals = None
	for column in train_x:
		curr_attribute = train_x[column]
		result = type_of_category(curr_attribute)
		entropy_vals.append(info_gain_entropy(curr_attribute))
	#sorts the data-frame columns
	#builds a tree


def info_gain_entropy(data_series):
	'''

	:param data_series:
	:return:
	'''
	
	return 1

def gini_idx(data_series):
	'''

	:param data_series:
	:return:
	'''

def classification_error(data_series):
	'''

	:param data_series:
	:return:
	'''

def type_of_category(data_series):
	'''
	Find the kind of category so that the split-creator can know
	how many child-nodes stem from the parent-node
	:param data_series: Column to split
	:return: <string> category type
	'''
	unique_elements = set(data_series)
	if len(unique_elements) == 2:
		return 'binary'
	elif len(unique_elements) <=6 and len(unique_elements) > 2:
		return 'categorical'
	elif len(unique_elements) == 1:
		return 'redundant'
	else: return 'continuous'