import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='en', help='Choose language')

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--disable-notifications')
        # options.add_argument('--start-maximized')
        # options.add_argument('--start-fullscreen')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')
        print('\nTime::{}'.format(datetime.today().strftime('%d.%m.%Y::%H:%M:%S::')))
        print("\nStart CHROME browser for test..")
        browser = webdriver.Chrome(options=options)
        # browser = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
        browser.maximize_window()
    elif browser_name == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nStart FIREFOX browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nQuit browser..")
    browser.quit()

