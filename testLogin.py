import allure
import pytest


@pytest.fixture(scope="class", params=["userName", "Password"])
def lgin(request):
    # 相当于setUp
    username = request.param
    print("登入...")
    yield username
    # 相当于tearDown
    print("...登出")


@allure.feature("模拟登录")
class TestLg():
    def test_case1(self):
        print("打开登录页面")

    @allure.story("为什么作用域设置了class级别,但还是function级别调用??")
    def test_case2(self, lgin):
        print(f"输入用户名&密码")

    def test_case3(self):
        print("点击登录")
