# MySQL



## 开始

###   启动与停止（以管理员身份打开cmd）

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230720092428.png)

  ### 连接客户端

+ 

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230720092900.png)

+ 

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230720093124.png)



## 仓库的操作

### 数据库操作

~~~mysql
# 如果不存在名为changku的仓库则创建，并以utf8mb4为字符集
create database if not exists changku default charset utf8mb4;

# 展示当前所操作的数据库
show database;

# 查询当前数据库 
select database();

# 删除数据库
drop database if exists changku;

# 使用
use changku;
~~~



### 数据类型

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230720150821.png)

+ 无符号类型则在后面加unsigned就行

+ double(4, 1)整个长度为4只允许出现一位小数

---

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230720152028.png)

+ 变长字符串会根据你所存储的字符串长度来决定存储内存
+ 定长字符串则由一开始就决定内存大小

---

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230720152629.png)

---

### 运算符

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230720191021.png)

![1689851460123](C:\Users\k\AppData\Roaming\Typora\typora-user-images\1689851460123.png)

---

### 表操作

- #### 基本操作

~~~mysql
# 查询数据库所有表
show tables;

# 创建表,comment后面可以加注释,如果是字符型用varcahr(字符串长度)替换int
 create table my_table(
 id int comment '@',
 age int comment '#'
 ) comment '1';

# 查询表结构
desc my_table;

# 查询指定表的建表语句(更详细的表结构,显示注释) 
show create table my_table;

# 删除字段sex
alter table my_table drop sex;

# 修改表名
alter table my_table rename to my_newtable;

# 删除表
drop table if exists my_table;

# 删除指定表并重新创建该表
truncate table my_table;
~~~



- #### 修改、添加字段

~~~mysql
# 添加字段
alter table my_table add gender char(1) comment '性别';

# 修改字段
alter table my_table change gender sex char(1) comment '将gender改为sex';

# 对字段插入单行数据
insert into my_table(id, age, gender) values (1, 2, 'a');# 可以指定字段进行数据插入
insert into my_table values (1, 2, 'a');  # 对全部字段进行数据插入

# 对字段插入批量数据
insert into my_table(id, age, gender) values (1, 2, 'a'),(2, 3, 'b'),(),();
insert into my_table values (1, 2, 'a'),(2, 3, 'b'),(),();
~~~

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230720162009.png)



- #### 修改和删除

~~~mysql
# 修改数据(将id=1且age=2的那行数据的id改为100，age改为19)，不加where就在所有行执行这个操作
update my_table set id = 100, age = 19 where id = 1 and age =2;

# 删除数据(不能删除某一个字段的值，update可以实现这个要求，delete则是删除整一行或多行的值)
delete from my_table where 
~~~

- #### 查询

~~~mysql
# 查询字段age和id的数据，'年龄'(as '年龄')是age的重命名在展示的时候age会显示成'年龄'
select age '年龄'，id from my_table;

# 查询返回所有字段
select * from my_table;

# 查询返回的数据不重复
select distinct age '年龄' from my_table;

# 条件查询
select * from my_table where age = 100;  # 还有<,<=,!=或<>,betweeb x and y(闭区间且x<y)
select * from my_table where age in (18,19);  # 年龄为18或19的数据
select * from my_table where age is null;  # 没有填写年龄的数据
select * from my_table where age is not null;  # 有填写年龄的数据
select * from my_table where name like '__';  # 名字两个字符的数据(字符数即划线个数)
select * from my_table where name like '%A';  # 名字最后一个字符为A的数据
 
 # 利用聚合函数查询(null值不参与计算)
 select count(*) from my_table;  # 查询整个表的数据量
 select count(id) from my_table;  # 查询id这一列的数据量
 # avg()求平均，max()求最大值，min()求最小值，sum()求和
 
~~~

~~~mysql
# 分组查询
# 根据年龄分组统计不同年龄的员工数量，前面的age要和后面的age相同
select age, count(*) from my_table group by age;
# 晒出年龄小于200的数据的数量且按id来分组，最后输出数量小于等于1的数据
select id ,count(*) from my_table where age<200 group by id having count(*)<= 1;
~~~

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230720193448.png)

where后面不能跟聚合函数，但having可以

---

~~~mysql
# 排序查询
# 将整行数据对年龄进行升序排序，如果年龄相同则按id升序排序，asc升序，desc为降序，默认为asc
select * from my_table order by age asc , id asc;
~~~

~~~mysql
# 分页查询
# 将第0到10行的数据放在一页展示出来
select * from my_table limit 0,10;
select * from my_table limit 10; # 与上面等价
~~~

+ #### 编写与执行顺序

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230721150547.png)

---

---

### 管理用户

+ #### 基本操作

~~~mysql
# 查询用户
use mysql;
select * from user;

# 创建用户 yang,只能在当前主机localhost访问，密码是123456（未分配权限）
create user 'yang'@'localhost' identified by '123456';

# 创建用户 yang,能在任意主机访问，密码是123456（未分配权限）
create user 'yang'@'%' identified by '123456';

# 修改用户访问密码，改为1234
alter user 'yang'@'localhost' identified with mysql_native_password by '1234';

# 删除用户
drop user 'yang'@'localhost';
~~~

---

+ #### 权限控制

![](https://shangxueweilong.oss-cn-guangzhou.aliyuncs.com/20230721160811.png)

~~~mysql
# 查询用户具有什么权限
show grants for 'yang'@'localhost';

# 授予权限tk这个数据库所有表的权限
grant all on tk.* to 'yang'@'localhost';

# 撤销权限tk这个数据库所有表的权限
revoke all on tk.* from 'yang'@'localhost';
~~~



## 函数

+ ### 字符串函数

~~~mysql
# 字符串拼接
select concat('hello','world');

# 全部转为小写
select lower('ASDSADsss');

# 全部转为大写
select upper('sdsdsdaaaAAA')

# 左填充,将‘1’填充到‘ab’的左边使字符串长度为4，若所要求的长度小于原先长度则会删除原字符串的字符(从右到左)
select lpad('ab', 1, '1');

# 右填充,将‘1’填充到‘ab’的右边使字符串长度为4，若所要求的长度小于原先长度则会删除原字符串的字符(从右到左)
select rpad('ab', 1, '1');

# 去除字符串头部与尾部的空格,没空格则不去除
select trim('         1 2345'         );

# 截取字符串'hello world'第一个字符到第七个字符(从1开始索引)
select substring('hello world', 1, 7);
~~~

---

+ ### 数值函数

~~~mysql
# 向上取整
select ceil(0.1);

# 向下取整
select floor(0.9);

# 求模运算
select mod(9,7);

# 0到1的随机数
select rand()

# 四舍五入,第一个数是需要进行操作的数，第二个数是要保留的小数位数
select round(3.5,2);  #output=3.5
select round(3.5,1);  #output=3.5
select round(3.58,1);  #output=3.6
select round(3.5,0);  #output=4
~~~

---

+ ### 日期函数

~~~mysql
# 当前年月日
select curdate();

# 当前时间时、分、秒
select curtime();

# 当前年月日，时分秒
select now();

# 当前年
select year(now());
select year(curdate());
select year(curtime());

# 当前月
select month(now());
select month(curdate());
select month(curtime());

# 当前日期
select day(now());
select day(curdate());
select day(curtime());

# 在当前时间往后推10天
select date_add(now(), interval 10 day);
# 在当前时间往后推11年
select date_add(now(), interval 11 year);

# 计算相差天数
select datediff('2023-7-21', '2023-8-24');  #负数
select datediff('2023-8-24', '2023-7-21');  #正数

# 查询所有员工的入职天数，并根据入职天数倒叙排序
select name, datediff(curdate(), time_in) as time_long from my_table order by time_long desc;
~~~

---

+ ### 流程函数

~~~mysql
# 1
select case '18' when '18' then '后生仔' when '10000' then '爆金币' else 'normal' end; #output=后生仔

select case '10000' when '18' then '后生仔' when '10000' then '爆金币' else 'normal' end; #output=爆金币

select case '20' when '18' then '后生仔' when '10000' then '爆金币' else 'normal' end; #output=normal

# 年龄大于18输出成年人，否则输出未成年人
case when age >= 18 then '成年人' else '未成年人' end;
~~~













