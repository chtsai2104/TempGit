import os

if os.path.exists('sketch.txt'):

    the_file = open('sketch.txt')

    for each_line in the_file:
        if not each_line.find(":") == -1:
            (role, line_spoken) = each_line.split(":", 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')

    the_file.close()

else:
    print("File not found!!")
