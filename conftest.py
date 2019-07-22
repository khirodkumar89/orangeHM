import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="type in browser")

@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:\\Users\\khirod\\PycharmProjects\\orangeHM\\drivers\\chromedriver.exe")
    else:
        driver = webdriver.Firefox(executable_path="C:\\Users\\khirod\\PycharmProjects\\orangeHM\\drivers\\geckodriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(15)
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test completed")