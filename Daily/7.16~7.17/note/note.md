### RestNet

+ 之间的神经网络当网络层数较多时会出现的问题：

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230717192707.png)

+ 基本框架

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230717192904.png)

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230717192941.png)





## ResNet的改进

+ 右边为改进模式

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230717193213.png)



![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230718120113.png)

---

+ 参数个数：

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230717193804.png)





## Dropout补充

+ ***背景***：在Dropout之前，正则化是主要的用来缓解模型过拟合的策略，例如l1正则和l2正则。但是它们并没有完全解决模型的过拟合问题，原因就是网络中存在co-adaption（共适应）问题。

  所谓co-adaption，是指网络中的一些节点会比另外一些节点有更强的表征能力。这时，随着网络的不断训练，具有更强表征能力的节点被不断的强化，而更弱的节点则不断弱化直到对网络的贡献可以忽略不计。这时候只有网络中的部分节点才会被训练，浪费了网络的宽度和深度，进而导致模型的效果上升收到限制。

  而Dropout的提出解决了co-adaption问题，从而使得训练更宽的网络成为可能。

+ 缩放问题：

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230718182704.png)





## BN补充

+ ***计算均值和方差，以一个channel为单位：***

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230718185457.png)

---

+ 在验证时training参数设置为False不意味着不需要BN了而是采用之前训练集的历史统计的均值和方差

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230718185832.png)

---

+ ***相关参数：***初始时γ为1，β为0

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230718190202.png)





## 训练过程中一个Batch的图片数据实际上是如何参与训练的？

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230718200449.png)















