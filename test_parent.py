import pytest

from testdata import Testdata

@pytest.mark.usefixtures("page")
class Parent_test(Testdata):
    

    pass