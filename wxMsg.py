import time

def textMsg(ToUserName,FromUserName,Content):
    xmlText ="""
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """.format(ToUserName=FromUserName,FromUserName=ToUserName,CreateTime=int(time.time()),Content=Content)
    return xmlText

def imageMsg(ToUserName,FromUserName,PicUrl):
    return "Success"
