#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import datetime

os.system("ipython /home/jovyan/work/crawler/netcwl.ipynb")
os.system("ipython /home/jovyan/work/crawler/GAP.ipynb")
os.system("ipython /home/jovyan/work/crawler/uni.ipynb")
os.system("ipython /home/jovyan/work/crawler/suit.ipynb")
# os.system("ipython /home/jovyan/work/usernotes.ipynb")
# os.system("ipython /home/jovyan/work/modelconfirm.ipynb")
# os.system("ipython /home/jovyan/work/log_mongo.ipynb")

while True:
        # 判斷是否達到設定時間，例如0:00
    while True:
        now = datetime.datetime.now() + datetime.timedelta(hours=8)
        # 到達設定時間，結束內循環
        if now.hour==6 and now.minute==0:
            break
                
    os.system("ipython /home/jovyan/work/crawler/netcwl.ipynb")
    os.system("ipython /home/jovyan/work/crawler/GAP.ipynb")
    os.system("ipython /home/jovyan/work/crawler/uni.ipynb")
    os.system("ipython /home/jovyan/work/crawler/suit.ipynb")
#     os.system("ipython /home/jovyan/work/log_mongo.ipynb")


# In[2]:





# In[ ]:




