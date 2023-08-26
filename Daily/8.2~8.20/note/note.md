# LSTM

+ 长短期记忆（Long short-term memory, LSTM）是一种特殊的RNN，主要是为了解决长序列训练过程中的梯度消失和梯度爆炸问题。简单来说，就是相比普通的RNN，LSTM能够在更长的序列中有更好的表现。

+ 结构

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/202308231724966.png)

生动揭示lstm原理[【LSTM长短期记忆网络】3D模型一目了然，带你领略算法背后的逻辑_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1Z34y1k7mc/?spm_id_from=333.337.search-card.all.click&vd_source=569f086a419ab937dcceef0145f29d01)



# 高德地图的API接口

+ 过程

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/202308231733896.png)

+ 

在网址https://lbs.amap.com/dev/申请一个Web服务开发的Key，如下图所示

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/202308231837594.png)



+ 代码

~~~python
def geocode(location):
	# 参数内容 可以写成字典的格式
	parameters = {'output': 'json', 'key': '8deff3f066215ffdb311a5d678a7e99b','location': 	  location, 'extensions':'all'}
	# 问号以前的内容
	base = 'http://restapi.amap.com/v3/geocode/regeo'
	response = requests.get(base, parameters)
	print('HTTP 请求的状态: %s' %response.status_code)
	print('url : %s'%response.url)
	print('编码格式: %s'%response.encoding)
	#print(response.text)
	# 查看网页的编码：Response Header中可以获取编码格式 charset= utf-8
	# 参考https://blog.csdn.net/w_linux/article/details/78370218
	#answer = response.json()
	return response.json()

if __name__ == '__main__':
	loc = str(101)+ ','+str(25)  #经纬度
	data = geocode(loc)  # 获取的数据类型为dict
	print(type(data))
	print(type(data['regeocode']))
	print(data['regeocode'])
	'''
	for key, value in data['regeocode'].items():
		print(key)
		print(value)
	'''
	formatted_address = data['regeocode']['formatted_address']
	for key, value in data['regeocode']['addressComponent'].items():
		print('%s : %s' %(key,value))
	print(formatted_address)
~~~



# 墨卡托投影法

+ 将经纬度进行转换
+ 公式

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/202308231849214.png)



# page rank

+ 作用：Page Rank是定义在网页集合上的一个函数，它对每个网页给出一个正实数，表示网页的重要程度，整体构成一个向量，Page Rank值越高，网页就越重要，在互联网搜索的排序中可能就被排在前面。

详见：[PageRank算法详解 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/137561088)



