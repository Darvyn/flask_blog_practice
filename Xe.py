#coding:utf-8
'''
通过xe网站爬取汇率信息
'''
__author__ = 'Xavier Yang'

import requests
from bs4 import BeautifulSoup
import dialogs
import sys

lst = ['CNY-人民币','EUR-欧元','USD-美元','TWD-新台币','MUR-毛里求斯卢比','JPY-日元','HKD-港币','MAD-摩洛哥迪拉姆']
headers = {'user_agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def main():
  ask_from = dialogs.list_dialog('From:', lst)
  if not ask_from:
    sys.exit()
  from_num = dialogs.input_alert('How much:','','1')
  ask_to = dialogs.list_dialog('To:',lst)
  if not ask_to:
    sys.exit()
  url = 'http://www.xe.com/zh-CN/currencyconverter/convert/?Amount={0}&From={1}&To={2}'.format(from_num, ask_from, ask_to)
  try:
    open = requests.get(url, headers=headers)
  except requests.RequestException as e:
    print(e)
    sys.exit()
  soup = BeautifulSoup(open.text, 'html.parser')
  result = soup.find('span', class_='uccResultAmount').text
  date = soup.find('span', class_='resultTime').text
  print('\n\n','~'*5,date,'~'*5)
  print(' {} {} = {} {}'.format(from_num, ask_from[4:], result, ask_to[4:]))

  

 
if __name__ == '__main__':
  a = main()
  

  
  
