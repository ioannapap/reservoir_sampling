import sys

def check_input():

	if len(sys.argv) != 4:

		print('Wrong format. Try: "reservoir.py" "sample_number" "<" "input_file.txt"')
		sys.exit(-1)


def reservoir_sampling():











if __name__ == '__main__':

	check_input()

	with open(input_file, 'r', encoding='UTF-8') as std_in:

		row = std_in.readline()

		while row != ' ':

			sampled_row = reservoir_sampling(row) 

			with open('output.txt', 'w+', encoding='UTF-8') as std_out:

				std_out.writelines('%s\n' % sampled_row)

			try:

				row = std_in.__next__() 	

			except StopIteration:

				print('End of file')

