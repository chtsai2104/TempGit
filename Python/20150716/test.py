try:

    #the_file = open('sketch.txt')
    with open('sketch.txt') as the_file:

        try:
            for each_line in the_file:
                (role, line_spoken) = each_line.split(':', 1)
                print(role, end='')
                print(' said: ', end='')
                print(line_spoken, end='')

        except ValueError as err:
            print("Value Error: " + str(err))

except IOError as err:
    print("File Error: " + str(err))

"""    
finally:
    if 'the_file' in locals():
        the_file.close()
"""
