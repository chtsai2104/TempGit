man = []
other = []

try:

    the_file = open('sketch.txt')

    for each_line in the_file:
        try:
            (role, line_spoken) = each_line.split(":", 1)
            """
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
            """
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass

    the_file.close()

except IOError:
    print("File not found!!")

try:
    #利用with語法開啟檔案並進行寫入動作
    with open('man_data.txt', 'w') as man_file:
        for each_item in man:
            print(each_item, file=man_file)
            
    with open('other_data.txt', 'w') as other_file:
        for each_item in other:
            print(each_item, file=other_file)    
    
except IOError:
    print("File not found!!")

#因為使用了with來處理檔案，所以不需要寫finally了
"""
finally:
    if 'man_file' in locals():
        man_file.close()
    if 'other_file' in locals():
        other_file.close()
""" 
