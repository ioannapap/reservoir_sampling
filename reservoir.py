#Ioanna Papapianni

import sys
import random


def check_input():

	if len(sys.argv) != 2:

		print('Wrong format. Try:\n python3 reservoir.py "sample_number_K" "<" "input_file.txt"')
		sys.exit(-1)

	if int(sys.argv[1]) <= 0:

		sys.exit(-1)


def reservoir_sampling(K, row, row_number, selected_rows):

	if random.random() < min(1, (K / row_number)):

		if len(selected_rows) < K:
			
			selected_rows.insert(len(selected_rows), row)

		else:

			random_place = random.randint(0, len(selected_rows)-1)
			selected_rows[random_place] = row

	return selected_rows


def print_rows(sampled_rows):

	for i in range(len(sampled_rows)):

		if sampled_rows[0] != '':
			print('%d. %s' % (i + 1, sampled_rows[i]))


if __name__ == '__main__':

	check_input()

	K = int(sys.argv[1])	

	with open('input.txt', 'r', encoding='UTF-8') as std_in:

		row = std_in.readline()
		row_number = 1
		sampled_rows = []

		while row != ' ':

			sampled_rows = reservoir_sampling(K, row, row_number, sampled_rows)
			#print(sampled_rows)

			try:

				row = std_in.__next__()
				row_number += 1

			except StopIteration:

				break

	print_rows(sampled_rows)
	
