import os

index = 0

try:
    for each_file in os.listdir():
        if each_file.endswith('txt'):
            with open(each_file, 'r') as data_file:
                data = data_file.readline()
                file = each_file.split('.')
                print(file)
                file[0] = data.strip().split(',')
                print(file[0])
                
except IOError as err:
    print('IO Error: ' + str(err))
