import pytest
import yaml

from HogwartsLG5.calculator.calculator import Calculator


def get_data(path):
    with open(path) as f:
        datas_list = yaml.safe_load(f)
        data = datas_list["datas"]
        myids = datas_list["myids"]
        return [data,myids]

get_calc = Calculator()
class TestCalc:
    def setup_method(self):
        print("开始计算")
    def teardown_method(self):
        print("结束计算")
    @pytest.mark.parametrize("a,b,expected", get_data("clacdata.yml")[0], ids=get_data("clacdata.yml")[1])
    def test_add(self,a,b,expected):
        result_add = get_calc.add(a,b)
        assert result_add == expected

    @pytest.mark.parametrize("a,b,expected", get_data("sub_data.yml")[0], ids=get_data("sub_data.yml")[1])
    def test_sub(self,a,b,expected):
        result_sub = get_calc.sub(a,b)
        assert result_sub == expected

    @pytest.mark.parametrize("a,b,expected", get_data("mul_data.yml")[0], ids=get_data("mul_data.yml")[1])
    def test_mul(self,a, b, expected):
        result_mul = get_calc.mul(a, b)
        assert result_mul == expected

    @pytest.mark.parametrize("a,b,expected", get_data("div_data.yml")[0], ids=get_data("div_data.yml")[1])
    def test_div(self,a,b,expected):
        result_div = get_calc.div(a,b)
        assert result_div == expected