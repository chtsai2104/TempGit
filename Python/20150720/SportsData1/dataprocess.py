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

    #可將上述的for loop動作改用列表推導的方式完成
    #clean_james = [sanitize(each_time) for each_time in james]

    #列印Copied Sorting的結果進行觀察
    print(sorted(clean_james))
    print(sorted(clean_julie))
    print(sorted(clean_mikey))
    print(sorted(clean_sarah))
    
except IOError as err:
    print('IO Error: ' + str(err))
