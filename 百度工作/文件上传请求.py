import requests

headers = {
    "Authorization": "v_zhangyang30",
    "accept": "*/*",
}
f = open("C://Users/13792/Desktop/下载内容/输入法/11.6.12.2.apk", "rb")
resp = requests.post(
    "https://quick.baidu-int.com/api/file/app",
    headers=headers,
    files={"file": f},
    data={
        "branchName": "release_11_6_10_0",
        "productId": 1347058356187308033,
        "type": "apk",
    }, )
print(resp.status_code)
print(resp.text)