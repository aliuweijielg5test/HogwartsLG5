import os

import pytest
import yaml

# 通过os.path.dirname获取当前文件所在路径
# path =os.path.dirname(__file__)+"./add_data.yml"

def datas(path):
    with open(path) as f:
        datas = yaml.safe_load(f)
        #获取文件中key为datas的数据
        re_datas = datas["datas"]
        # 获取文件中key为myids的数据
        re_ids = datas["myids"]
        return re_datas,re_ids

@pytest.fixture(params = datas("./add_data.yml")[0],ids = datas("./add_data.yml")[1])
def add_datas(request):
    print("开始计算")
    data = request.param
    yield data
    print("结束计算")

@pytest.fixture(params = datas("./sub_data.yml")[0],ids = datas("./sub_data.yml")[1])
def sub_datas(request):
    print("开始计算")
    data = request.param
    yield data
    print("结束计算")

@pytest.fixture(params = datas("./mul_data.yml")[0],ids = datas("./mul_data.yml")[1])
def mul_datas(request):
    print("开始计算")
    data = request.param
    yield data
    print("结束计算")

@pytest.fixture(params = datas("./div_data.yml")[0],ids = datas("./div_data.yml")[1])
def div_datas(request):
    print("开始计算")
    data = request.param
    yield data
    print("结束计算")


class TestCalc():

    def test_add(self,get_calc,add_datas):
        result_add = get_calc.add(add_datas[0],add_datas[1])
        assert result_add == add_datas[2]

    def test_sub(self,get_calc,sub_datas):
        result_sub = get_calc.sub(sub_datas[0],sub_datas[1])
        assert result_sub == sub_datas[2]

    def test_mul(self,get_calc,mul_datas):
        result_mul = get_calc.mul(mul_datas[0],mul_datas[1])
        assert result_mul == mul_datas[2]

    def test_div(self,get_calc,div_datas):
        result_div = get_calc.div(div_datas[0],div_datas[1])
        assert result_div == div_datas[2]