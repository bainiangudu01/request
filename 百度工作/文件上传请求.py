import requests

headers = {
    "Authorization": "v_zhangyang30",
    "accept": "*/*",
}
f = open("/Users/v_zhangyang30/Downloads/11.7.0.22.apk", "rb")
resp = requests.post(
    "https://quick.baidu-int.com/api/file/app",
    headers=headers,
    files={"file": f},
    data={
        "branchName": "feature_196_merge_koom",
        "productId": 1347058356187308033,
        "type": "apk",
    }, )
print(resp.status_code)
print(resp.text)
