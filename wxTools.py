import time
def GetMiddleStr(content,startStr,endStr):
    startIndex = content.index(startStr)
    if startIndex>=0:
        startIndex += len(startStr)
    endIndex = content.index(endStr)
    return content[startIndex:endIndex]

def wxLog(txt):
    '''
    Log函数
    :param txt:
    :return:
    '''
    logPath = "Log.txt"
    text = "["+getTime()+"]"+"    "+txt+"\n"
    print(text)
    try:

        with open(logPath,"a") as f:
            text = "[" + getTime() + "]" + "    " + txt + "\n\n"
            f.write(text)
    except FileNotFoundError as e:
            pass




def getTime(Datatime=None):
    '''

    用于格式化时间

    :param Datatime:时间数据
    :return:格式化后的时间
    '''
    if Datatime == None:
        Datatime = time.localtime()
        nowTime = time.strftime("%Y/%m/%d %H:%M:%S", Datatime)

    if Datatime == 'hour':
        Datatime = time.localtime()
        nowTime = time.strftime("%H", Datatime)

    # print(time.strftime("%Y-%m-%d %H:%M %p", time.localtime()))
    return nowTime