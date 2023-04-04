import requests

resp = requests.get("https://baidu.com", json={"a": 1})  # 响应
print(resp.status_code)  # 状态码
print(resp.url)  # 地址，因为url是在请求中的，若以相当于resp.request.url
print(resp.headers)  # 响应头
print(resp.cookies)  # 在http协议中，cookies属于headers一部分
print(resp.content)  # 打印二进制模式的正文，得到二进制的数据流，是字节，以b开头
resp.encoding = "utf-8"
print(resp.encoding)
print(resp.text)  # 打印字符串模式的正文（会自动将二进制转为字符串）
if "json" in resp.headers.get("Content-Type"):
    # 如果是json内容，才会按照json方式解析
    print(resp.json())
    # 打印json模式的正文，这是方法，需要加括号，此url响应正文非字典，用不了
