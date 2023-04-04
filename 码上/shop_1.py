import requests
from session import Session

session = Session("http://101.34.221.219:8010/api.php")
session.params = {
    "s": "index/index",
    "application": "web",
    "application_client_type": "android",
    "token": ""
}

resp = session.get(
    "",
    params={
        "s": "index/index",
    },
)

resp = session.post(
    "",
    params={
        "s": "goods/detail",
    },
    json={"goods_id": "12"},
)
