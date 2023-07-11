### 使用tensorboard绘制函数，展示图片

~~~
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


~~~
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

~~~

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


~~~
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

