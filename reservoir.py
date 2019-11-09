import sys
import random

def check_input():

	if len(sys.argv) != 2:
		print(len(sys.argv))
		print(sys.argv)
		print('Wrong format. Try: "reservoir.py" "sample_number" "<" "input_file.txt"')
		sys.exit(-1)


def reservoir_sampling(K, row, row_number, selected_rows):

	if row_number == 1:
		
		selected_rows = []

	if len(selected_rows) < K:

		if random.randint(1, row_number) < K:

			selected_rows.insert(len(selected_rows), row)

	else:
		s = int(random.random() * row_number)
		if s < K:
	
			selected_rows[s] = row

	return selected_rows

#https://web.archive.org/web/20141026071430/http://propersubset.com:80/2010/04/choosing-random-elements.html

def print_rows(sampled_rows):

	for i in range(len(sampled_rows)):

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
			print(sampled_rows)
			try:

				row = std_in.__next__()
				row_number += 1

			except StopIteration:

				break

	print_rows(sampled_rows)


