# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 15:07:53 2018

@author: 12434
"""

import http.client
import hashlib
import json
import urllib
import random
 
 #定义百度api对比模型翻译
def baidu_translate(content):
    appid = '你的百度api id'
    secretKey = '你的百度api的idkey'
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = content
    fromLang = 'zh' # 源语言
    toLang = 'en'   # 翻译后的语言
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign
 
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        jsonResponse = response.read().decode("utf-8")# 获得返回的结果，结果为json格式
        js = json.loads(jsonResponse)  # 将json格式的结果转换字典结构
        dst = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果
        print(dst) # 打印结果
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
 
if __name__ == '__main__':
    while True:
        print("请输入要翻译的内容,如果退出输入q")
        content = input()
        if (content == 'q'):
            break
        baidu_translate(content)
