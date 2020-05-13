# :whale:AutoRge-Rc3

自动生成锐格实验报告的程序

学会为有用的程序加星:star:是一种美德:kissing_heart:

## :rocket:原理

借助selenium控制浏览器自动制作实验报告，至于为什么不用beautiful soup—— 

懒得去分析网页了，加上锐格本身代码就不是很好分析，写的太乱了，所以我认为selenium是最好的解决方案了

## :black_nib:依赖

由于本项目是基于浏览器+python实现的，所以依赖项如下：

1. python>=3.6
2. chrome 81
3. pyperclip==1.7.0
4. python-docx==0.8.10
5. selenium==3.141.0

安装步骤：

1. 安装python3，具体教程请参照网络
2. 首先安装chrome，保证版本为81，以避免出现驱动兼容性问题
3. 打开cmd命令，请将目录切换至本项目目录后
   执行：` pip install -r requirements.txt`
   或者：`pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple`
   等待安装结束

## :memo:程序说明

#### 1.主程序入口：main.py

第一次打开会要求输入vpn账号等信息，请如实填写，

如果填写错误，请执行init.py程序以修正信息

#### 2.实验总结

程序预设了三个实验总结样本，请视情况自己修改实验总结文本

目录：`/settings/zjie.json`

#### 3.mb.docx文件

这个就是模板了，请在使用前填写自己的姓名以及学号，

保存后即可开始运行程序，请勿直接使用群内的doc文件，

:warning:**该程序不支持doc文件！！！**:warning:

#### 4.bug反馈

请直接在github提交issue！！！

请直接在github提交issue！！！

请直接在github提交issue！！！

不要在qq或者其他地方给我留言，请学会使用github这个平台！！！

#### 5.目前已知Bug

-[ √] 实验总结是能使用三个