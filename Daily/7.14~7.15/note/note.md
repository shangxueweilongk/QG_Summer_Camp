## 感受野

+ **概念**：在卷积神经网络中,感受野(Receptive Field)是指特征图上的某个点能看到的输入图像的区域,即特征图上的点是由输入图像中感受野大小区域的计算得到的

+ **计算公式**:这里的层数有坑，原来的公式也对看怎么看待第一层

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230714215330.png)



## Batch Normalization

[什么是批标准化 (Batch Normalization) - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/24810318)





## GoogLeNet

+ 示意图

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230716083351.png)

+ **inception**：采取并联结构，使得特征矩阵的深度降低，极大的减少了参数，进而减少了计算量。


+ **辅助分类器：**给定深度相对较大的网络，有效传播梯度反向通过所有层的能力是一个问题。在这个任务上，更浅网络的强大性能表明**网络中部层产生的特征应该是非常有识别力的**。通过将辅助分类器添加到这些中间层，可以期望较低阶段分类器的判别力。这被认为是在**提供正则化的同时克服梯度消失问题**。这些分类器采用较小卷积网络的形式，放置在Inception (4a)和Inception (4b)模块的输出之上。在训练期间，它们的损失以折扣权重（辅助分类器损失的权重是0.3）加到网络的整个损失上。在推断时，这些辅助网络被丢弃。后面的控制实验表明辅助网络的影响相对较小（约0.5），只需要其中一个就能取得同样的效果。

---





## 迁移学习

+ 过程![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230716090230.png)

![1689469391697](C:\Users\k\AppData\Roaming\Typora\typora-user-images\1689469391697.png)

+ 优点：

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230716090157.png)