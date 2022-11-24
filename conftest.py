import pytest
from Tools.scripts.fixdiv import report
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
driver=None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        if browser_name == "chrome":
            # chrome_path = r"C:/Users/deepa/quantium-starter-repo/quantium-starter-repo/chromedriver.exe"
            ser = Service(r"C:/Users/deepa/Desktop/deepa/JustRecharge/chromedriver.exe")
            op = webdriver.ChromeOptions()
            s = webdriver.Chrome(service=ser, options=op)
            driver = webdriver.Chrome(s)

            #driver = webdriver.Chrome(executable_path=r"C:/Users/deepa/quantium-starter-repo/quantium-starter-repo/chromedriver.exe")
        
    url="http://127.0.0.1:8050/"
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(20)
    request.cls.driver = driver
    yield
    driver.close()
    return driver

   