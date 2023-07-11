# BilibiliTicketRushBuy
 bilibili会员购抢票脚本，使用时需自行设置相关参数
## 参数设置
抢购时间设置：Main.py第12行

目标抢购页面设置：Main.py第17行

选择是否使用headless游览器：Main.py第15、16行

场次选择：Main.py第20行

价格选择：Main.py第21行
## 环境
python == 3.10

Google Chrome == 正式版

## 使用流程
1.按照上述操作设置好相关参数

2.在项目所在路径打开cmd

3.依次输入以下指令并运行：
```
pip install -r requirements.txt
python Main.py
```
4.若有正常输出，则程序正常运行，请等待出现名为qrimg的窗口（其中内容为bilibili账号登录页面截图），待扫码登录后关闭qrimg窗口，随后程序将自动运行，无需额外操作。
## TODO
1.多线程运行

2.可视化页面
## 注意事项
若pip安装出现网络问题，可尝试使用以下命令进行安装
```
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```


使用程序前，请保证网络畅通和电脑时间为北京时间。

本程序仅适用与bilibili会员购抢票，一切因本项目引起的经济问题，本项目不负任何责任。并且此项目无法保证100%抢票成功，请将此项目作备用手段而非唯一手段使用
