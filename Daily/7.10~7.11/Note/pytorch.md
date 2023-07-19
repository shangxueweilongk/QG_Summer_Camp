### 使用tensorboard绘制函数，展示图片

~~~python
#导包
from torch.utils.tensorboard import SummaryWriter
writer =SummaryWriter("logs")
import numpy as np
from PIL import Image

#存储图片路径
image_path="dataset/train/ants/9715481_b3cb4114ff.jpg"
img=Image.open(image_path)

#转为为nparray，展示图片
img_array=np.array(img)
writer.add_image("demo",img_array,2,dataformats='HWC')#dataformats='HWC'指定每一维的含义

#绘制函数
for i in range(100):
    writer.add_scalar("y=x",i,i)
writer.close()
~~~



### 使用tensor上面是用nparray


~~~python
from torchvision import transforms
from PIL import Image
from torch.utils.tensorboard import SummaryWriter

img_path="dataset/train/ants/9715481_b3cb4114ff.jpg"
img=Image.open(img_path)
writer=SummaryWriter("logs")

#转化为tensor上面是用nparray
tensor_trans=transforms.ToTensor()
tensor_img=tensor_trans(img)

writer.add_image("tensor_img",tensor_img)
writer.close()
~~~



### Transforms的操作

~~~python

from torchvision import transforms
from PIL import Image
from torch.utils.tensorboard import SummaryWriter

writer =SummaryWriter("logs")
img = Image.open("dataset/train/ants/9715481_b3cb4114ff.jpg")
tensor_trans=transforms.ToTensor()
tensor_img=tensor_trans(img)

#1改变图片像素 Normalize
trans_norm=transforms.Normalize([0.5,0.5,0.5],[0.5,0.5,0.5])
img_norm=trans_norm(tensor_img)

writer.add_image("Normalize",img_norm)
writer.close()


#2改变图片大小1 Resize
trans_resize=transforms.Resize((512,512))#(512,512)为大小
img_resize=trans_resize(img)

img_resize=tensor_trans(img_resize)

writer.add_image("Resize",img_resize,0)


#3改变图片大小2 Compose -resize
trans_resize2=transforms.Resize(512)
trans_compose=transforms.Compose([trans_resize2,tensor_trans])
#将image传进去
img_resize2=trans_compose(img)
writer.add_image("Resize",img_resize2,1)


#4随机裁剪
trans_random=transforms.RandomCrop(100)
trans_compose2=transforms.Compose([trans_random,tensor_trans])
#共十张
for i in range(10):
    img_crop=trans_compose2(img)
    writer.add_image("RandomCrop",img_crop,i)
writer.close()


~~~



### datasets和DataLoader


~~~python
import torchvision

#下载图片
train_set=torchvision.datasets.CIFAR10(root="./data1",train=True,transform=torchvision.transforms.ToTensor(),download=True)
test_set=torchvision.datasets.CIFAR10(root="./data1",train=False,transform=torchvision.transforms.ToTensor(),download=True)

writer=SummaryWriter("p10")
for i in range(15):
    img,target=test_set[i]#target指向标签，一个target对于一个标签
    writer.add_image("test_set",img,i)
writer.close()

###############################################################
###############################################################
from torch.utils.data import DataLoader

test_data=torchvision.datasets.CIFAR10("./data1",train=False,transform=torchvision.transforms.ToTensor())
"""
batch_size每次抽取图片的数量（随机）；shuffle即”洗牌“，每次（times）抽取都可能不一样；
drop_last最后一次不满36是否取出，true则取出;num_workers多进程，=0则为主进程
"""
test_loader=DataLoader(dataset=test_data,batch_size=36,shuffle=True,num_workers=0,drop_last=True)

writer=SummaryWriter("dataloder")
for times in range(2):
    step=0
    for data in test_loader:
        imgs,targets=data
        writer.add_images("times: {}".format(times),imgs,step)
        step+=1
writer.close()

~~~



### torch和ToTensor的区别

~~~
x=torch.tensor(1.0) ##正确的
y=transforms.ToTensor(2.0) ##错误的，不能输入数字会报错，只接受PIL和numarray
~~~



### 图像标准化与归一化

+ 归一化：归一化后，不同维度之间的特征在数值上有一定比较性，可以大大提高分类器的准确性

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230713153643.png)

+ 标准化后，最优解的寻优过程明显会变得平缓，更容易正确的收敛到最优解

*详见：[一文读懂图像数据的标准化与归一化图像标准化的意义·城府、的博客-CSDN博客](https://blog.csdn.net/qq_45704645/article/details/111089328)*

[(32条消息) 图像标准化与归一化_怎么显示归一化后的图像_niuniubeibeikzh的博客-CSDN博客](https://blog.csdn.net/niuniubeibeikzh/article/details/105286867?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-105286867-blog-115267174.235^v38^pc_relevant_anti_vip&spm=1001.2101.3001.4242.1&utm_relevant_index=3)

### X.view()

+ **x.view()就是对tensor进行reshape：**

  在某一个维度，我们可以传入数字-1，自动对维度进行计算并变化：

  假设我们有一个数据维度为【3，5，2】的tensor，我们想要将其转化为其中两个维度分别为【3，1】，【5，2】，而剩下的第三个维度自动进行计算，那么我们可以使用-1来代替【3，1，10】当中的10，以及用-1来代替转化后【5，2，3】维度当中的数字3.我们可以发现3x1x10=3x5x2=5x2x3，因此变化后的维度乘积是相等的。

~~~python
import torch
v1 = torch.range(1, 4)
v2 = v1.view(2, 2)
print(v2)
v3 = v2.view(4,-1)
print(v3)
~~~

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230713154109.png)





### F.relu() 与 nn.ReLU() 的区别

+ 其实这两种方法都是使用relu激活，只是使用的场景不一样，F.relu()是函数调用，一般使用在foreward函数里。而nn.ReLU()是模块调用，一般在定义网络层的时候使用。

~~~python
import torch.nn as nn
import torch.nn.functional as F

class NET1(nn.Module):
    def __init__(self):
        super(NET1, self).__init__()
        self.conv = nn.Conv2d(3, 16, 3, 1, 1)
        self.bn = nn.BatchNorm2d(16)
        self.relu = nn.ReLU()  # 模块的激活函数

    def forward(self, x):
        out = self.conv(x)
        x = self.bn(x)
        out = self.relu()
        return out


class NET2(nn.Module):
    def __init__(self):
        super(NET2, self).__init__()
        self.conv = nn.Conv2d(3, 16, 3, 1, 1)
        self.bn = nn.BatchNorm2d(16)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        out = F.relu(x)  # 函数的激活函数
        return out


net1 = NET1()
net2 = NET2()
print(net1)
print(net2)
~~~

+ 参数inplace的作用：降低内存

[(32条消息) 激活函数nn.ReLU(inplace=True)中inplace的作用_relu inplace=true_HealthScience的博客-CSDN博客](https://blog.csdn.net/weixin_43135178/article/details/115477790?ops_request_misc=%7B%22request%5Fid%22%3A%22168931939216800222873188%22%2C%22scm%22%3A%2220140713.130102334..%22%7D&request_id=168931939216800222873188&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-115477790-null-null.142^v88^insert_down1,239^v2^insert_chatgpt&utm_term=relu里面的inplace参数&spm=1018.2226.3001.4187)

## iter()

[(32条消息) Pytorch中iter(dataloader)的使用_沐雲小哥的博客-CSDN博客](https://blog.csdn.net/weixin_44533869/article/details/110856518)



## softmax

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230719093943.png)



## Pytorch中shuffle=True的作用

[(32条消息) Pytorch中shuffle=True的作用_pytorch shuffle_Z字君的博客-CSDN博客](https://blog.csdn.net/zzc_zhuyu/article/details/116659157?ops_request_misc=%7B%22request%5Fid%22%3A%22168933820316800182146004%22%2C%22scm%22%3A%2220140713.130102334..%22%7D&request_id=168933820316800182146004&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-2-116659157-null-null.142^v88^insert_down1,239^v2^insert_chatgpt&utm_term=shuffle%3Dtrue&spm=1018.2226.3001.4187)





## torch.bmm

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230719193031.png)

[(33条消息) torch.bmm()函数解读_wang xiang的博客-CSDN博客](https://blog.csdn.net/qq_40178291/article/details/100302375)



## torch.randn()

+ 返回一个符合均值为0，方差为1的[正态分布](https://so.csdn.net/so/search?q=正态分布&spm=1001.2101.3001.7020)（标准正态分布）中填充随机数的张量

+ ~~~python
  >>> torch.randn(4)
  tensor([-2.1436,  0.9966,  2.3426, -0.6366])
  >>> torch.randn(2, 3)
  tensor([[ 1.5954,  2.8929, -1.0923],
          [ 1.1719, -0.4709, -0.1996]])
  
  ~~~



## torch.cat()

~~~python
a = torch.randn(2,3)
b =  torch.randn(3,3)
c = torch.cat((a,b),dim=0)
a,b,c

输出结果如下：
(tensor([[-0.90, -0.37,  1.96],
         [-2.65, -0.60,  0.05]]),
 tensor([[ 1.30,  0.24,  0.27],
         [-1.99, -1.09,  1.67],
         [-1.62,  1.54, -0.14]]),
 tensor([[-0.90, -0.37,  1.96],
         [-2.65, -0.60,  0.05],
         [ 1.30,  0.24,  0.27],
         [-1.99, -1.09,  1.67],
         [-1.62,  1.54, -0.14]]))


a = torch.randn(2,3)
b =  torch.randn(2,4)
c = torch.cat((a,b),dim=1)
a,b,c

输出结果如下：
(tensor([[-0.55, -0.84, -1.60],
         [ 0.39, -0.96,  1.02]]),
 tensor([[-0.83, -0.09,  0.05,  0.17],
         [ 0.28, -0.74, -0.27, -0.85]]),
 tensor([[-0.55, -0.84, -1.60, -0.83, -0.09,  0.05,  0.17],
         [ 0.39, -0.96,  1.02,  0.28, -0.74, -0.27, -0.85]]))


~~~

[(32条消息) Pytorch中torch.cat()函数解析_cv_lhp的博客-CSDN博客](https://blog.csdn.net/flyingluohaipeng/article/details/125038212?ops_request_misc=%7B%22request%5Fid%22%3A%22168938767016800182122769%22%2C%22scm%22%3A%2220140713.130102334..%22%7D&request_id=168938767016800182122769&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-125038212-null-null.142^v88^insert_down1,239^v2^insert_chatgpt&utm_term=torch.cat&spm=1018.2226.3001.4187)











































