import csv, statistics, numpy as np
debug = True
data_ext = []
data_app = []
no_of_features = 0
data_loader = []

'''def load_data():
	with open('student/student-mat.csv', 'r') as csvfile:
		data_reader = csv.reader(csvfile, delimiter=';', quotechar='"')
		next(data_reader)
		for row in data_reader:
			data_loader = row
			#print(data_loader)
			data_ext.extend(data_loader)
			data_app.append(data_loader)
#end of load_data
'''

def load_data():
	data = np.loadtxt('students/student-mat.csv',
	                  #dtype={'names':('school','sex','age','address','famsize','pstatus', 'medu', 'fedu', 'mjob', 'fjob', 'reason', 'guardian', 'traveltime', 'studytime','failures','schoolsup','famsup','paid', 'activities', 'nursery', 'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'dalc', 'walc', 'health', 'absences', 'g1', 'g2', 'g3'),
	                   #      'formats':('S1','S1','i4','S1','S1','S1','i4', 'i4', 'S1', 'S1', 'S1' )},
	                  delimiter=',',
	                  usecols=(0,2)
	                  )

def clean_data():
	if debug:
		print(data_ext)
		print("Now printing append")
		print(data_app)
		#print(len(data))
		#print(data[:][0]==data[0][:])
		#print([sub_list[0] for sub_list in data])
		#print(data[23])
	#for i in range(0, no_of_features):
	#school_name = [sub_list[0] for sub_list in data]

def numerize(str_list):
	print(str_list)
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