import pytest
import yaml
from calculator import Calcula
from decimal import Decimal


class TestCalculate:
    def setup_class(self):
        self.calculus = Calcula()
        self.ids = []
        print("\n【测试开始】")

    def teardown_class(self):
        print("\n【测试结束】")

    def setup(self):
        print("\n【正在计算...】")

    def teardown(self):
        print("\n【计算完毕！】")

    @pytest.mark.parametrize("name, a, b, result", yaml.safe_load(open("./data_case_add.yaml", 'r', encoding='utf-8')),
                             ids=[i[0] for i in yaml.safe_load(open("./data_case_add.yaml", 'r', encoding='utf-8'))])
    def test_add(self, name, a, b, result):
        print(name)
        assert Decimal(str(result)) == self.calculus.add(Decimal(str(a)), Decimal(str(b)))

    @pytest.mark.parametrize("name, a, b, result", yaml.safe_load(open("./data_case_div.yaml", 'r', encoding='utf-8')),
                             ids=[i[0] for i in yaml.safe_load(open("./data_case_div.yaml", 'r', encoding='utf-8'))])
    def test_div(self, name, a, b, result):
        print(name)
        if b == 0:
            pytest.xfail(reason='除数不能为零！,跳过！')
        else:
            assert Decimal(str(result)) == self.calculus.div(Decimal(str(a)), Decimal(str(b)))
