# -*- coding: utf-8 -*-
import requests #HTTP通信ライブラリ
from bs4 import BeautifulSoup #HTMLから狙ったデータを抽出するライブラリ
#import re 
#import pandas as pd
#import time

#pages = [1, 2, 3, 4, 5]

for page in range(100):
    res = requests.get('https://tabelog.com/tokyo/rstLst/' + str(page) + '/?Srt=D&SrtT=rt&sort_mode=1&svd=20201014&svt=1900&svps=1')
    soup = BeautifulSoup(res.text, 'html.parser')
    quote_elms = soup.find_all('a', {'class': 'list-rst__rst-name-target'})
    for t in quote_elms:
        print(t.text)