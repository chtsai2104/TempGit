import os

index = 0
data_list = []

try:
    for each_file in os.listdir():
        if each_file.endswith('txt'):
            with open(each_file, 'r') as data_file:
                data = data_file.readline()
                data_list[index] = data.strip().split(',')
                index += 1
except IOError as err:
    print('IO Error: ' + str(err))
