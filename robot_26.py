# -*- coding: utf-8 -*-
import xmpp

user = "youmirobot@gmail.com"
password = "iloveUMLife123"
server="gmail.com" 
resource = "Script"


#robot 开始发送消息
def chat(msg):

    jid = xmpp.protocol.JID(user) 
    connection = xmpp.Client(jid.getDomain(),debug=[]) 
    connection.connect(("talk.google.com",5222)) 
    result = connection.auth(jid.getNode(), password,resource) 
    connection.sendInitPresence()

    fp = open("contactlist","r")
    for line in fp: 
        to = line[0:-1]
        message = xmpp.Message(to, msg)
        message.setAttr('type', 'chat')
        connection.send(message)
    fp.close()


if __name__ == '__main__':
    msg = "please ignore me ! i am just test"
    chat(msg)
