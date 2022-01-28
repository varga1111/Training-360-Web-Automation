import pytest
from selenium import webdriver

from testdata import Testdata


@pytest.fixture(params=['chrome'], scope ='class')
def init_driver(request):

    if request.params == 'chrome':
        browser = webdriver.Chrome(executable_path=Testdata.PATH)
    
    request.cls.browser = browser
    yield
    browser.close()
