import urllib.parse

d = {
    'referer': 'http%3A%2F%2F47.107.116.139%2Fphpwind%2Fread.php%3Ftid%3D16341%26fid%3D2',
    'refresh': True,
    'state': 'success',
    'data': '',
    'html': '',
    'message': ['操作成功'],
    '__error': ''
}
url = urllib.parse.unquote(d["referer"])
print(url)
tid = urllib.parse.parse_qs(url)['http://47.107.116.139/phpwind/read.php?tid'][0]
print(tid)
