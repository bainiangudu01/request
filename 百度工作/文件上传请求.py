import requests

headers={
    "Request-Origion":"SwaggerBootstrapUi",
    "Authorization":"v_zhangyang30",
    "accept":"*/*",
    "Content-Type":"multipart/form-data"
}
resp = requests.post(
    "https://quick.baidu-int.com/api/file/app",
    headers=headers,
    data={
        "branchName": "release_11_6_9_0",
        "productId": 1347058356187308033,
        "Authorization": "v_zhangyang30",
        "file": "C:\\Users\13792\Desktop\下载内容\输入法apk\11.6.9.19.apk",
        "type": "apk",
    }, )
print(resp.status_code)
print(resp.text)
