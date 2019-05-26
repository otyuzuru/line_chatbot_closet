#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import datetime
# from datetime import datetime
from os import listdir
from linebot import LineBotApi
from linebot.models import TextSendMessage
import os
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, PostbackEvent
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageMessage, ImagemapSendMessage, BaseSize,
    URIImagemapAction, ImagemapArea, TemplateSendMessage, URITemplateAction, ButtonsTemplate, 
    ConfirmTemplate, PostbackTemplateAction, MessageTemplateAction, DatetimePickerAction, CarouselColumn, CarouselTemplate
)
import time
import json
import shutil
import pymysql

secretFileContentJson=json.load(open("/home/jovyan/work/line_secret_key",'r'))
server_url=secretFileContentJson.get("server_url")


line_bot_api = LineBotApi(secretFileContentJson.get("channel_access_token"))


while True:
    mypath = "/home/jovyan/work/images/userdate"

    files = listdir(mypath)
    

    for fn in files:
        if not fn == ".ipynb_checkpoints" and not fn == 'readme.txt':
            

            if os.path.isfile("/home/jovyan/work/images/userdate/" + fn + "/" + fn.split('_')[1] + ".txt"):

                if fn.split('_')[0] == (datetime.datetime.now() + datetime.timedelta(hours=8)).strftime("%Y-%m-%dT%H:%M"):

                    try:
                        with open("/home/jovyan/work/images/userdate/" + fn + "/" + fn.split('_')[1] + ".txt",'r',encoding="utf-8") as fd:

                            msg = fd.read().split(',')


                        user_add1 = ImageSendMessage(original_content_url=server_url + "/images/userdate/" + fn + "/" + fn.split('_')[1] + ".jpg",
                                                    preview_image_url=server_url +"/images/userdate/" + fn + "/" + fn.split('_')[1] + ".jpg")

                        db = pymysql.connect("mysql","root","iii","user_data" )
                        cursor = db.cursor()
                        cursor.execute('select * from line_user where line_id = '+ '"' + msg[0] + '"' )
                        results = cursor.fetchone()
                        
                        line_bot_api.push_message(msg[0],[TextSendMessage(text='使用者 '+results[1]+ ' 您好'),
                                                          TextSendMessage(text='您有一項活動即將進行'),
                                                          TextSendMessage(text='情境: '+msg[1]), 
                                                          TextSendMessage(text='活動: '+msg[2]), user_add1])
            #             time.sleep(5)
                        os.remove("/home/jovyan/work/images/userdate/" + fn + "/" + fn.split('_')[1] + ".txt")
#                         shutil.rmtree("./images/userdate/" + fn)
                    except:
                        pass
        
            if datetime.datetime.strptime(fn.split('_')[0], '%Y-%m-%dT%H:%M') < (datetime.datetime.now() + datetime.timedelta(hours=7)):

                shutil.rmtree("/home/jovyan/work/images/userdate/" + fn)


    


# In[ ]:




