# 益书网自动登陆签到
本项目在python3下开发。

由于目前益书网是https加密，模拟请求登陆比较麻烦，所以直接使用selenium进行登陆签到

>本项目在运行5个月后无疾而终。益书网于2018.2关闭了服务器。告别益书网!

## 如何运行
推荐使用docker，也可直接python运行：

需要先安装phantomjs，这是一个无头浏览器，地址为：
http://phantomjs.org/download.html
解压到你的本地或者服务器上，并记下解压后的地址

将config.yml.bak 改名为 config.yml 
然后参照上面的格式，填写对应的用户名等参数

### docker
在本项目目录下运行
docker build -t auto-sign .
docker run -d --name auto-sign auto-sign

### python3
先安装依赖
pip3 install -r requirements.txt
然后后台运行
python sign.py &

## 定时以及消息推送
本项目采用server酱的微信推送功能，具体见百度。如果不需要该功能，将msg方法注释掉即可
定时推送，采用cron类型，每天7点定时登陆签到。
