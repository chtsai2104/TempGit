import os

os.chdir('SportsData1')

index = 0

try:
    for each_file in os.listdir():
        with open(each_file, 'r') as data_file:
            data = data_file.readline()
            data_list = data.strip().split(',')
            print(data_list)
except IOError as err:
    print('IO Error: ' + str(err))
