import time
import requests
import urllib.parse
from session import Session

session = Session()
session.params = {"fid": 2}

resp = session.get("http://47.107.116.139/phpwind/")
print(resp.text)

csrf_token = resp.cookies.get("csrf_token")  # 从响应的cookies中获取csrf_token

# CSRF攻击，跨站请求网站，通过JS代码，从A网站向B网站发送请求
# 故要求，只能从A网站向A网站发送请求，从B网站向B网站发送请求
# 原理：第一次访问：设置cookies
#     第二次访问：验证cookies
resp = session.post(
    "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun",
    headers={
        "Accept": "application/json, text/javascript, /; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
    },
    data={
        "username": "beifan",
        "password": "beifan",
        "csrf_token": csrf_token,
        "backurl": "http://47.107.116.139/phpwind/",
    },
)
print(resp.text)

# 3.登录成功后跳转接口
url = urllib.parse.unquote(resp.json()["referer"])  # 对接口2返回的url进行解析，转成正常的url
resp = session.get(url)
assert "beifan" in resp.text  # 判断登录成功

# 7.发帖接口
content = f"zhangyang{time.time()}"  # 时间戳
resp = session.post(
    "http://47.107.116.139/phpwind/index.php?c=post&a=doadd&_json=1",
    data={
        "atc_title": content,
        "atc_content": content,
        "csrf_token": csrf_token,
        "pid": "",
        "reply_notice": 1,
        "special": "default",
        "tid": "",
    },
)
print(resp.json())
assert "success" in resp.text

# 9.回帖接口
time.sleep(4)  # 有灌水机制
url = urllib.parse.unquote(resp.json()["referer"])
tid = urllib.parse.parse_qs(url)['http://47.107.116.139/phpwind/read.php?tid'][0]
resp = session.post(
    "http://47.107.116.139/phpwind/index.php?c=post&a=doreply&_getHtml=1",
    data={
        "atc_content": "回帖124",
        "csrf_token": csrf_token,
        "tid": tid,
    }
)
print(resp.text)
