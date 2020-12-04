import allure
import pytest
import yaml


def get_yaml(tp):
    with open("./yaml_data.yml", encoding="utf-8") as file:
        datas = yaml.safe_load(file)
    if tp == "data":
        return datas['data']
    if tp == "step":
        return datas["step"]


def get_steps(tp, calc, a, b, expect):
    steps = get_yaml(tp)
    for tp in steps:
        if "add" == tp:
            result = calc.add(a, b)
        elif "add2" == tp:
            result = calc.add(a, b)
        elif "add1" == tp:
            result = calc.add(a, b)

        assert result == expect


@allure.feature("测试计算器")
class TestCalc():
    @allure.story("加法_正常")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize(["a", "b", "expect"], get_yaml('data')["add"]["datas"], ids=get_yaml('data')['add']['ids'])
    def test_add(self, get_calc, a, b, expect):
        pytest.assume(get_calc.add(a, b) == expect)

    @allure.story("加法_异常case1")
    @pytest.mark.parametrize(["a", "b", "expect"],
                             [["a", "b", "c"], ["a", "1", "a1"], [1 + 1, 2 - 0, 4], [0.1 + 0.2, 0.1 + 0.1, 0.5]])
    def test_add1(self, get_calc, a, b, expect):
        pytest.assume(get_calc.add(a, b) == expect)

    @allure.story("加法_类型错误")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize(["a", "b", "expect"],
                             [[None, None, None], ["a", 1, "a1"]])
    def test_add2(self, get_calc, a, b, expect):
        with pytest.raises(TypeError):
            get_calc.add(a, b)

    @pytest.mark.run(order=1)
    @allure.story("加法: 数据驱动")
    def test_add3(self, get_calc):
        a = 1
        b = 1
        expect = 2
        get_steps('step', get_calc, a, b, expect)

    @pytest.mark.run(order=4)
    @allure.story("除法")
    @pytest.mark.parametrize(["a", "b", "expect"], get_yaml('data')["div"]["datas"],
                             ids=get_yaml("data")['div']['ids'])
    def test_div(self, a, b, expect, get_calc):
        pytest.assume(get_calc.div(a, b) == expect)

    @pytest.mark.run(order=4)
    @allure.story("除法_类型错误")
    @pytest.mark.parametrize(["a", "b", "expect"],
                             [[None, None, None], ["a", 1, "a1"]])
    def test_div1(self, get_calc, a, b, expect):
        with pytest.raises(TypeError):
            get_calc.div(a, b)

    @pytest.mark.run(order=2)
    @allure.story("减法")
    @pytest.mark.parametrize(["a", "b", "expect"], get_yaml('data')["sub"]["datas"],
                             ids=get_yaml("data")['sub']['ids'])
    def test_sub(self, a, b, expect, get_calc):
        pytest.assume(get_calc.sub(a, b) == expect)

    @pytest.mark.run(order=2)
    @allure.story("减法_异常")
    # @allure.attach("<h3>减法:反向用例</h3>", "描述", attachment_type=allure.attachment_type.HTML)
    @pytest.mark.parametrize(["a", "b", "expect"],
                             [["a1", "1", "a"], [1 + 1, 1 - 0, 1], [0.1 + 0.2, 0.1 + 0.5, -0.3]])
    def test_sub1(self, a, b, expect, get_calc):
        pytest.assume(get_calc.sub(a, b) == expect)

    @pytest.mark.run(order=3)
    @allure.story("乘法")
    # @allure.attach('''<h3>正向用例</h3>''',"描述",attachment_type=allure.attachment_type.HTML)
    @pytest.mark.parametrize(["a", "b", "expect"], get_yaml('data')["mul"]["datas"],
                             ids=get_yaml("data")['mul']['ids'])
    def test_mul(self, a, b, expect, get_calc):
        pytest.assume(get_calc.mul(a, b) == expect)

    @pytest.mark.run(order=3)
    @allure.story("乘法_异常")
    # @allure.attach('''<h3>反向用例</h3>''', "描述", attachment_type=allure.attachment_type.HTML)
    @pytest.mark.parametrize(["a", "b", "expect"],
                             [["a1", 1, "a"], [1 + 1, 1 - 0, 2], [0.1 + 0.2, 0.1 + 0.5, 0.18]])
    def test_mul1(self, a, b, expect, get_calc):
        pytest.assume(get_calc.mul(a, b) == expect)
