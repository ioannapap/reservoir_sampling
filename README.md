# reservoir_sampling

A modified Reservoir Sampling algorithm that samples Κ items from a stream of N items, uniformly at random, so that each element has probability K/N to appear in the sample. The
algorithm should work in a single pass over the data, reading the items one by one, without prior knowledge of the size of the stream N, and using O(Κ) of memory.
              
SETUP: (Prerequisite: Python)

This algorithm is implemented in Python3 and runs with the following command line format in Terminal:
>> python3 reservoir.py sample_number_K < input_file.txt

sample_number_K:  any positive integer number

input_file.txt:   any .txt file

Note that, it is necessary for the files to be in the same exact folder and run the above Terminal
commands in that exact folder.
