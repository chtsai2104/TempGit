#定義函數將傳入的時間字串進行處理並回傳想要的格式
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif '.' in time_string:
        splitter = '.'
    else:
        return(time_string)

    (mins, secs) = time_string.strip().split(splitter)

    return(mins + ':' + secs)


#開啟檔案並切割資料
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

    #呼叫sanitize函數將時間格式化成 min:sec
    """
    clean_james = []
    clean_julie = []
    clean_mikey = []
    clean_sarah = []

    for each_time in james:
        clean_james.append(sanitize(each_time))    
    for each_time in julie:
        clean_julie.append(sanitize(each_time))
    for each_time in mikey:
        clean_mikey.append(sanitize(each_time))
    for each_time in sarah:
        clean_sarah.append(sanitize(each_time))
    """

    #可將上述的for loop動作改用列表推導的方式完成
    clean_james = sorted(set([sanitize(each_time) for each_time in james]))
    clean_julie = sorted(set([sanitize(each_time) for each_time in julie]))
    clean_mikey = sorted(set([sanitize(each_time) for each_time in mikey]))
    clean_sarah = sorted(set([sanitize(each_time) for each_time in sarah]))
    print(clean_james[0:3])
    print(clean_julie[0:3])
    print(clean_mikey[0:3])
    print(clean_sarah[0:3])

    #去除重複性的資料
    unique_james = []
    for each_t in clean_james:
        if each_t not in unique_james:
            unique_james.append(each_t)

    print(unique_james[0:3])

    unique_julie = []
    for each_t in clean_julie:
        if each_t not in unique_julie:
            unique_julie.append(each_t)

    print(unique_julie[0:3])

    unique_mikey = []
    for each_t in clean_mikey:
        if each_t not in unique_mikey:
            unique_mikey.append(each_t)

    print(unique_mikey[0:3])

    unique_sarah = []
    for each_t in clean_sarah:
        if each_t not in unique_sarah:
            unique_sarah.append(each_t)

    print(unique_sarah[0:3])
    
except IOError as err:
    print('IO Error: ' + str(err))
