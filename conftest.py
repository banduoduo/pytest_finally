"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/11 3:05 下午'
"""
# @pytest.fixture()
# def login():
#     print("这是企业微信的登录")

import pytest

from Hogwarts_pytest_2.pytestdemo.demo1.pytest_works.Calculator import Calculator


def pytest_collection_modifyitems(session, config, items: list):
    print("搜集所有的测试用例方法")
    print(items)
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


@pytest.fixture(scope='class')
def calc_class():
    calc = Calculator()
    yield calc
    print("teardown")


@pytest.fixture(params=[[1, 1, 1], [10000, 1000, 11000]], ids=['加整型', '加整型1'])
def get_add_calc(request):
    return request.param


def test_add_calc(get_add_calc):
    print(get_add_calc)

    # @pytest.fixture(params=get_datas()['int_datas'], ids=get_datas()['ids'])
    # def get_datas_calc(request):
    #     return request.param
    #
    # def test_get_datas(get_datas_calc):
    #     print(get_datas_calc)


@pytest.fixture(params=[
    [0.1, 0.1, 0.2], [0.4, 0.8, 1.2]], ids=['加浮点数', '加浮点数1'])
def get_add_calc1(request):
    return request.param


def test_add_calc1(get_add_calc):
    print(get_add_calc)


@pytest.fixture(params=[[1, 1, 0], [20, 10, 10]], ids=['less_int', 'less_int1'])
def get_less_calc(request):
    return request.param


def test_less_calc():
    print(get_less_calc)


@pytest.fixture(params=[[0.5, 0.1, 0.4], [1.8, 0.8, 1]], ids=['减浮点数', 'less_float1'])
def get_less_calc1(request):
    return request.param


@pytest.fixture(params=[[1, 1, 1], [1000, 1, 1000]], ids=['div_int', '除整型'])
def get_div_calc(request):
    return request.param


@pytest.fixture(params=[[0.4, 0.2, 0.2], [10, 1, 10]], ids=['div_float', 'div_float1'])
def get_div_calc1(request):
    return request.param


@pytest.fixture(params=[[0, 1, 0], [10, 0, 0]], ids=['div_zero', 'div_zero1'])
def get_div_calc2(request):
    return request.param


@pytest.fixture(params=[[1, 1, 1], [1000, 1, 1000]], ids=['mul_int', 'mul_int1'])
def get_mul_calc(request):
    return request.param


@pytest.fixture(params=[[0.4, 0.2, 0.08], [10, 1, 10]], ids=['乘浮点数', 'mul_float1'])
def get_mul_calc1(request):
    return request.param
