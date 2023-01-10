# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 19:30:57 2023

@author: Administrator
"""
import requests
import base64

# 百度AI开放平台鉴权函数
def get_access_token():
    url = 'https://aip.baidubce.com/oauth/2.0/token'
    data = {
        'grant_type': 'client_credentials',  # 固定值
        'client_id': '7qGKEXsdUbeg5l5Hmsbl057t',  # 在开放平台注册后所建应用的API Key
        'client_secret': 'MpC7Urn6p8HUL1Wv6dqs4GZbz4L6N9ci'  # 所建应用的Secret Key
    }
    res = requests.post(url, data=data)
    res = res.json()
    print(res)
    access_token = res['access_token']
    return access_token

access_token = get_access_token() # 获取access tocken的时候需要保证没有vpn在运行

#通用文字识别
def general_word(r_path,w_path):
    #通用文字识别接口url
    general_word_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    #获取执行路径
    # path = os.getcwd()
    # 二进制方式打开图片文件
    f = open(r_path, 'rb')
    img = base64.b64encode(f.read())
    print(img)
    params = {"image":img,
              "language_type":"CHN_ENG"}
    access_token = get_access_token()
    request_url = general_word_url + "?access_token=" + access_token
    print(request_url)
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    # print(response)
    # res = response.json()
    if response:
        res = response.json()["words_result"]
        print(res)
        file_name = w_path
        with open(file_name, 'w', encoding='utf-8') as f:
            for j in res:
                print(j["words"])
                f.write(j["words"]+"\n")


if __name__ == '__main__':
    r_path = 
    w_path = 
    general_word()