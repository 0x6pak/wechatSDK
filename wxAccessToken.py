import SQL
import requests
import json
import wxTools
import os
import gc
import time

class ATSQL():

    def __init__(self):
        self.wxTable = "wxAT"
        self.wxTableValues = "(id int, time text, AT text)"
        self.createSQL()

    def createSQL(self):
        '''
        查询并创建一个表
        :return:
        '''
        if ezSQL.likeSQL(self.wxTable) == False:
            #print(False)
            ezSQL.createSQL(self.wxTable,self.wxTableValues)


    def insAT(self,id,time,AT):
        '''
        插入时间数据和AT
        :return:
        '''
        ezSQL.delSQL(self.wxTable,'id = 1') #删除上一条数据 让数据库保持只有一条AT数据
        ezSQL.insSQL(self.wxTable,'({id}, \"{time}\", \"{AT}\")'.format(id=id,time=time,AT=AT))




class AT:



    def getAT(self):
        jsonText = requests.get("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx8f490f350bd104b2&secret=c3f85bebb144636b26451ffdd97c40eb",verify=False).content.decode("utf-8")
        jsonData = json.loads(jsonText)
        access_token = jsonData['access_token']
        # self.getNextTime()

        SQL.insAT(1,wxTools.getTime(),access_token)

        del jsonData
        del jsonText
        gc.collect()
        return access_token

    def getNextTime(self):  #已废弃 当做参考
        nowHour = wxTools.getTime("hour")
        nextTime = ""
        if nowHour == "23":
            nextTime = "01"
        if nowHour == "24":
            nextTime = "02"
        if nextTime == "":
            nextTime = str(int(nowHour) + 2)
        with open("ATNextTime.txt","w") as f:
            f.write(nextTime)

        del nowHour
        del nextTime
        gc.collect()





def getATHous():  #已废弃 当做参考
    nowHour = wxTools.getTime("hour")


    with open("ATNextTime.txt","r") as f:
        getHour = f.read()

    if getHour == "":
        AT.getAT()

    if int(nowHour) == int(getHour):
        AT.getAT()

    del nowHour
    del getHour
    gc.collect()









if __name__ == "__main__":
    if os.path.exists("ATNextTime.txt"):
        os.remove("ATNextTime.txt")
    ezSQL = SQL.ezSQL()
    SQL = ATSQL()
    #SQL.insAT(1, "sj", "dd")
    AT = AT()
    print(AT.getAT())
    while True:
        time.sleep(3600) #每个小时获取一次AT
        getATHous()


'''
微信的中控服务

获取AccessToken

'''



