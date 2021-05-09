import pytest

from pytest_cal_fixture.calculator import Calculator


@pytest.fixture(scope="module")
def get_calc():
    #实例化类,生成类的对象
    print("获取计算器实例")
    calc = Calculator()
    return calc
