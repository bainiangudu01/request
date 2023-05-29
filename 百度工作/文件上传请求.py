import requests

headers = {
    "Authorization": "v_zhangyang30",
    "accept": "*/*",
}
f = open("C:/Users/13792/Desktop/下载内容/输入法/10.6.121.82wd.apk", "rb")
resp = requests.post(
    "https://quick.baidu-int.com/api/file/app",
    headers=headers,
    files={"file": f},
    data={
        "branchName": "dev_oem_10_6_121_0_xiaomi_new",
        "productId": 1347058356187308033,
        "type": "apk",
    }, )
print(resp.status_code)
print(resp.text)
