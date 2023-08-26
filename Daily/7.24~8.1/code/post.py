import requests
from flask import json

url = 'http://39.98.41.126:31130/ais/ln'
url_2 = 'http://39.98.41.126:31130/ais/jn'

# POST方式上传数据
# 验证的信息
post_dict_1 = {'username': 'A', 'password': '123456'}
post_dict_2 = {'want': 'B', 'group': "flower"}
files = {'file': open('test.txt', 'rb')}

post_dict_1 = json.dumps(post_dict_1)  # 转化成json形式发送
post_dict_2 = json.dumps(post_dict_2)  # 转化成json形式发送

headers = {'Content-Type': 'application/json'}  # 如果对方只接受application/json,需要加header
try:
    # 第一个请求验证身份
    response_1 = requests.post(url, data=post_dict_1, headers=headers)  # request请求发出去之后,返回一个来自服务器的response
    data_1 = response_1.json()  # 将响应数据解析为JSON格式（如果服务器返回JSON数据的话）  键值对的格式
    print(data_1)
    if data_1["code"] == 1001:
        print("用户身份验证成功！")

        # 第二个请求加入群组
        response_2 = requests.post(url_2, data=post_dict_2, headers=headers)
        data_2 = response_2.json()  # 将响应数据解析为JSON格式（如果服务器返回JSON数据的话）  键值对的格式
        if data_2["code"] == 1001:
            print("相应用户和组存在，可以加入")
        else:
            print("相应用户或组部不存在")
            exit()
    else:
        print("账户或密码出错")
        exit()

    # 第三个请求传数据(文件形式)
    response_3 = requests.post(url_3, files = files)
    

except requests.exceptions.RequestException as e:
    print("请求发生异常：", e)

