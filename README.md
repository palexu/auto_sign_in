# 益书网自动登陆签到
本项目在python3下开发。

由于目前益书网是https加密，模拟请求登陆比较麻烦，所以直接使用selenium进行登陆签到

## 如何运行
推荐使用docker，也可直接python运行，后者的运行方式如下：
先安装依赖
pip install -r requirments.txt

然后python运行本项目即可

## 定时以及消息推送
本项目采用server酱的微信推送功能，具体见百度。如果不需要该功能，将msg方法注释掉即可
定时推送，采用cron类型，每天7点定时登陆签到。
