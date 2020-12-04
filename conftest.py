# conftest是共享公共的fixture的,自动import的方法
# @pytest.fixture(autouse=True,scope="function")
# #autouse为True时,自动应用到每个方法里面,默认为False;scope默认是function级别的,还有class/module/package/session

# 如果项目有多个conftest文件,调用的是最近的那个

import pytest
import sys

sys.path.append('/Users/fg/PycharmProjects/projects/HogwartsSdet16/pytest_2_path')
from calculator_dome import Calculator


@pytest.fixture(scope='class')
def get_calc():
    print("计算开始...")
    calc = Calculator()
    yield calc
    print("...计算结束")


@pytest.fixture(autouse=True, scope='module')
def module_feature():
    print("+++++++++++" * 3)
    yield "module"
    print("-----------" * 3)


def pytest_collection_modifyitems(session, config, items):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
