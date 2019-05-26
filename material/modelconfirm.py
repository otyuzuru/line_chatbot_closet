#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from confluent_kafka import Consumer
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
import json

secretFileContentJson=json.load(open("/home/jovyan/work/line_secret_key",'r'))
server_url=secretFileContentJson.get("server_url")


line_bot_api = LineBotApi(secretFileContentJson.get("channel_access_token"))

props = {'bootstrap.servers': 'kafka4Br1:9092',
         'group.id': 'STUDENTID',
         'auto.offset.reset': 'earliest'}

consumer = Consumer(props)

topicName = "onionTopic2"

consumer.subscribe([topicName])

while True:

    records = consumer.consume()

    for record in records:

        msgValue = record.value()
        msgkey = record.key()

        try:
            clokk = str(msgValue, 'utf-8').split(',')[1][:-1]
            types = {"T-shirt": 'T-shirt', "Shirt": '襯衫', "Suit": '西裝外套', "Dress": '洋裝', "Vest": '背心'}
            clo = types[clokk]

            Confirm_template1 = TemplateSendMessage(
            alt_text='上傳確認',
            template=ConfirmTemplate(
            title='上傳確認',
            text='請問您上傳的是否為'+ clo + '呢?',
            actions=[                              
                PostbackTemplateAction(
                    label='是的',
                    data="Yc/" + str(msgValue, 'utf-8').split(',')[0][1:] + "/" + clo
                ),
                PostbackTemplateAction(
                    label='不是',
                    text='不是'+ clo +'，請換選項',
                    data= 'clo/' + str(msgValue, 'utf-8').split(',')[0][1:] + "/" + clo

                )
                ]
                )
                )
            line_bot_api.push_message(str(msgValue, 'utf-8').split(',')[0][1:],Confirm_template1)

        except:
            pass


# In[ ]:





# In[ ]:




