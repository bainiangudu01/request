import requests

headers = {
    "Content-Type": "application/json",
    "Cookie": [{
        "BAIDUID=424F28AF368D3B7AF5B3ADD383373CF2": "FG=1",
        "BAIDUID=A9F455BFE5A68673157FCFEC9A30070F": "FG=1",
        "BAIDUID_BFESS=1FD063F0BCF651FFC38FBAA80BF5CBBE": "FG=1"},
        "PHPSESSID=8sk096r88n3flv2s32d0qi4cj5"]
}
resp = requests.post(
    "https://mime-sh.baidu.com/imrobot/v0/pri/test/pe_push_strategy_unlimited",
    json={
        "user_status": 1,
        "uid": 2781443028,
        "strategy_type": 14,
        "lost_day": 0,
        "optional_strategy_id": 25,
    }, )
print(resp.status_code)
print(resp.text)
