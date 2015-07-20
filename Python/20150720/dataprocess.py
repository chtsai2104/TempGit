try:
    with open('james.txt', 'r') as jfile:
        data = jfile.readline()
        james = data.strip().split(',')
    with open('julie.txt', 'r') as jufile:
        data = jufile.readline()
        julie = data.strip().split(',')
    with open('mikey.txt', 'r') as mfile:
        data = mfile.readline()
        mikey = data.strip().split(',')
    with open('sarah.txt', 'r') as sfile:
        data = sfile.readline()
        sarah = data.strip().split(',')

    print(sorted(james))
    print(sorted(julie))
    print(sorted(mikey))
    print(sorted(sarah))
    
except IOError as err:
    print('IO Error: ' + str(err))
