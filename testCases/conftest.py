import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def setup(browser):
    if browser == 'firefox':
        options = webdriver.FirefoxOptions()
        # options.add_argument("detach", True)
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
        print("Launching firefox browser.........")
    else:
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features")
        options.add_argument("--disable-blink-features=AutomationControlled")  # by pass cloudfare processing
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        print("Launching chrome browser.........")

    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


########## pytest HTML Report ################

# # It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop Commerce'
#     config._metadata['Module Name'] = 'Customers'
#     config._metadata['Tester'] = 'Luke Ly'


# It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)

# # Specifying report folder location and save report with timestamp
# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     config.option.htmlpath = os.path.abspath(os.curdir) + "/reports/" + datetime.now().strftime(
#         "%d-%m-%Y %H-%M-%S") + ".html"
