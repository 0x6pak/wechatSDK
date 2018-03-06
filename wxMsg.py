import time
import wxTools


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


def xmlMsg(ToUserName,FromUserName,Title,Description,PicUrl,Url):
    xmlText = '''
    <xml>
        <ToUserName>< ![CDATA[{ToUserName}] ]>
        </ToUserName>
        <FromUserName>< ![CDATA[{FromUserName}] ]>
        </FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType>< ![CDATA[news] ]>
        </MsgType>
        <ArticleCount>1</ArticleCount>
        <Articles>
            <item>
                <Title>< ![CDATA[Title] ]>
                </Title>
                <Description>< ![CDATA[{Description}] ]>
                </Description>
                <PicUrl>< ![CDATA[{PicUrl] ]>
                </PicUrl>
                <Url>< ![CDATA[{Url}] ]>
                </Url>
            </item>
        </Articles>
    </xml>
    '''.format(ToUserName=FromUserName,FromUserName=ToUserName,CreateTime=int(time.time()),Description=Description,PicUrl=PicUrl,Url=Url)
    return xmlText





def subscribeEvent(ToUserName,FromUserName,Event):
    '''
    Event :subscribe为关注，unsubscribe为取消关注
    :return:
    '''
    wxTools.wxLog("收到事件~:"+Event)
    # return "Success"

    if Event == "subscribe":

       return textMsg(ToUserName,FromUserName,"谢谢关注本公众号")
    if Event == "unsubscribe":
        return "Success"