#import pandas as pd

#class IgesFile:
	#'''
	#Class to exploit CSV files from Sysmac Studio (OMRON)
	#'''
	#def __init__(self, path_file):
		#self.path_file = path_file
		#self.dataf = self.get_dataf()

	#def get_dataf(self):

		#dataf = pd.rea

path_text_file = 'C:\\Users\\guide\\Documents\\GitHub\\solidworks\\export_point.txt'

text_file = open(path_text_file, "r")

#text_file_data = text_file.read()

new_text_file_data = ''

x = 0
y = 0
marker_1 = 0
marker_2 = 0

#for line in text_file:
	##print(line)
	#for i, m in enumerate(line):
		#if m == ',':
			#marker_1 = i
			#x = line[:marker_1]
		#if m == ';':
			#marker_2 = i
			#y = line[marker_1:marker_2]
		#if i > marker_2:
			#m = ''

		##print(marker_1, marker_1)
		#new_text_file_data = new_text_file_data + m
	#new_text_file_data = new_text_file_data + '\n'


#new_text_file = open(path_text_file,"w")
#new_text_file.write(new_text_file_data)
#new_text_file.close()


tab_pos = []
sub_tab = [[], []]

for line in text_file:
	for i, m in enumerate(line):
		if m == ',':
			marker_1 = i
			x = float(line[:marker_1])
		if m == ';':
			marker_2 = i
			y = float(line[marker_1+1:marker_2])
		sub_tab[0].append(x)
		sub_tab[1].append(y)
		print(x,y)

	if line[:11] == 'next_sketch':
		print('___________________________________HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH')


text_file.close()
