## RNN

+ ***简单结构：***

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230719094610.png)

---

---

+ ***将输入进行处理：***

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230719094900.png)

---

---

+ ***损失函数***：与交叉熵二分类损失函数相似

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230719094850.png)

---

---

+ ***常见结构即应用：***

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230719095252.png)

---

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230719095542.png)

---

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230719095634.png)

+ ***优点与缺点：***

1. 能够解决序列问题、短期记忆型的任务
2. 容易产生梯度消失与梯度爆炸，前部序列信息传递到后部的时候，信息权重下降，导致重要信息丢失

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230719100718.png)

---

---

+ ***梯度裁剪：***

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230719101302.png)



























































