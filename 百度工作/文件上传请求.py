import requests

headers = {
    "Authorization": "v_zhangyang30",
    "Request-Origion": "SwaggerBootstrapUi",
    "accept": "*/*",
    "Content-Type": "multipart/form-data"
}
f = open("11.6.10.50.apk", "rb")
resp = requests.post(
    "http://10.161.18.17:0/api/file/app",
    headers=headers,
    files={"upload": f},
    data={
        "branchName": "release_11_6_10_0",
        "productId": 1347058356187308033,
        "type": "apk",
    }, )
print(resp.status_code)
print(resp.text)
