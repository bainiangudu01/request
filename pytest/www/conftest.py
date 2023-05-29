# import pytest
#
#
# def get_data():
#     return {"name": "百里"}, {"nam": "北凡"}, {"na": "天秋"}
#
#
# @pytest.fixture(scope="function", autouse=False, params=get_data(), name="es")
# def excute_sql(request):  # 固定写法
#     print("前置:sql查询")
#     yield request.param  # 固定写法
#     print("后置:关闭数据库连接")
