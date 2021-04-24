import pytest
import yaml

from pytest_cal.calculator import Calculator


def get_data(path):
    with open(path) as f:
        datas_list = yaml.safe_load(f)
        data = datas_list["datas"]
        myids = datas_list["myids"]
        return [data,myids]

get_cal = Calculator()
class TestCalc():
    def setup_method(self):
        print("开始计算")
    def teardown_method(self):
        print("结束计算")
    @pytest.mark.parametrize("a,b,expected", get_data("../pytest_cal/clacdata.yml")[0], ids=get_data(
        "../pytest_cal/clacdata.yml")[1])
    def test_add(self,a,b,expected):
        result_add = get_cal.add(a,b)
        assert result_add == expected

    @pytest.mark.parametrize("a,b,expected", get_data("../pytest_cal/sub_data.yml")[0], ids=get_data(
        "../pytest_cal/sub_data.yml")[1])
    def test_sub(self,a,b,expected):
        result_sub = get_cal.sub(a,b)
        assert result_sub == expected

    @pytest.mark.parametrize("a,b,expected", get_data("../pytest_cal/mul_data.yml")[0], ids=get_data(
        "../pytest_cal/mul_data.yml")[1])
    def test_mul(self,a, b, expected):
        result_mul = get_cal.mul(a, b)
        assert result_mul == expected

    @pytest.mark.parametrize("a,b,expected", get_data("../pytest_cal/div_data.yml")[0], ids=get_data(
        "../pytest_cal/div_data.yml")[1])
    def test_div(self,a,b,expected):
        result_div = get_cal.div(a,b)
        assert result_div == expected