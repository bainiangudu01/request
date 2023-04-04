import requests
from urllib.parse import urljoin
import logging

from requests import PreparedRequest, Response

logger = logging.getLogger("requests.session")  # 日志记录器，去记录日志
logging.basicConfig(level=logging.INFO)  # 指定日志级别


class Session(requests.Session):
    """
    封装，实现对BaseUrl的支持以及对日志记录的支持
    """

    def __init__(self, base_url=""):
        super().__init__()  # 调用父类方法，先按原有的方式实现实例化
        self.base_url = base_url  # 再按新的方式完成额外操作

    def request(self, method, url, *args, **kwargs):
        if not url.startswith("http"):  # 如果不是以http开头的
            url = urljoin(self.base_url, url)  # 就自动添加baseurl
        return super().request(method, url, *args, **kwargs)  # 按照原有方式执行

    def send(self, request: PreparedRequest, *args, **kwargs) -> Response:
        logger.info(f"发送请求>>>>>> 接口地址 = {request.method} {request.url}")
        logger.info(f"发送请求>>>>>> 请求头 = {request.headers}")
        logger.info(f"发送请求>>>>>> 请求正文 = {request.body}")
        resp = super().send(request, **kwargs)  # 按原有的方式发送请求
        logger.info(f"接收响应      <<<<<< 状态码 = {resp.status_code}")
        logger.info(f"接收响应      <<<<<< 响应头 = {resp.headers}")
        logger.info(f"接收响应      <<<<<< 响应正文 = {resp.content}")
        return resp


if __name__ == '__main__':
    session = Session("http://baidu.com")
    resp = session.get("/123")
    # 实际请求的地址是http://baidu.com/123
    print(resp.url)
