import os
import datetime

os.system("ipython /home/jovyan/work/crawler/weather_crawler.ipynb")

while True:
        # 判斷是否達到設定時間，例如0:00
    while True:
        now = datetime.datetime.now() + datetime.timedelta(hours=8)
        # 到達設定時間，結束內循環
        if now.hour==15 and now.minute==0 and now.second==0:
            break
                
    os.system("ipython /home/jovyan/work/crawler/weather_crawler.ipynb")