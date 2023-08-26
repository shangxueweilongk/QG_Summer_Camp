from flask import Flask, jsonify, request, url_for, redirect
import bao.my_try as mine
import time
import pandas as pd
import numpy as np

app = Flask(__name__)

pre,len = mine.arima()
t1 = time.localtime()
day = t1.tm_mday
print("#"*100)


@app.route("/1", methods=['POST', 'GET'])
def testT():
    day_now = day
    t2 = time.localtime()
    # 判断是否需要更新
    if t2.tm_mday != day_now:
        pre_1, len_1 = mine.arima()
        day_now = t2.tm_mday
        sum = pre_1.predict(len_1, len_1)
    else:
        sum = pre.predict(len, len)

    return {"USE":float(sum*6)}


@app.route('/', methods=['POST', 'GET'])  # 上面的request.get请求发送到api
def handle_request():
    accept = request.get_json()  # 接收到用户post的数据
    # 如果accept不是列表则转成列表
    if type(accept) != list:
        accept = [accept]

    # 转成dataframes形式
    accept2 = pd.DataFrame(accept)

    # 将dataframes转为列表形式
    turn = []
    for row in accept2.itertuples(index=False):
        turn.append(list(row))
    # 列表转为np数组
    final = np.array(turn).astype(float)
    print(final)

    return jsonify({'success': "成功了"})  # 通过jsonify将数据转换为JSON格式,返回给发post的用户


if __name__ == '__main__':
    app.run(host='0.0.0.0')

# requests和Flask是用于不同的任务：前者是用于发送HTTP请求，后者是用于创建服务器接收并处理HTTP请求。
# 在示例代码中，requests库被用于发送GET请求到另一个服务器（可能是某个API服务器），
# 而Flask库用于创建一个简单的Web服务器，处理客户端对/api路径的GET请求，并返回一个JSON响应。
