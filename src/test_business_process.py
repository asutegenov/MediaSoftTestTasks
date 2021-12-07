from src.pages.main_page import MainPage
from datetime import datetime, time
from src.pages.business_process import CheckBusinessProcess
import pytest

class TestGloriaJeans():
    # ОЖИДАЕМОЕ ПАДЕНИЕ
    @pytest.mark.xfail
    def test_registration(self, browser):
        start_time = datetime.now().timestamp()

        link = "https://www.gloria-jeans.ru"
        page = MainPage(browser, link)
        page.open()

        business_process = CheckBusinessProcess(browser, browser.current_url)

        business_process.registration()

        print('::-> ТЕСТ УСПЕШНО ПРОЙДЕН <-::')
        print("ВРЕМЯ ВЫПОЛНЕНИЯ::{:.3f}s".format(datetime.now().timestamp() - start_time))

    # @pytest.mark.skip
    def test_login_logout(self, browser):
        start_time = datetime.now().timestamp()

        link = "https://www.gloria-jeans.ru"
        page = MainPage(browser, link)
        page.open()

        business_process = CheckBusinessProcess(browser, browser.current_url)

        business_process.entrance()
        business_process.exit()

        print('::-> ТЕСТ УСПЕШНО ПРОЙДЕН <-::')
        print("ВРЕМЯ ВЫПОЛНЕНИЯ::{:.3f}s".format(datetime.now().timestamp() - start_time))

    # @pytest.mark.skip
    def test_search(self, browser):
        start_time = datetime.now().timestamp()

        link = "https://www.gloria-jeans.ru"
        page = MainPage(browser, link)
        page.open()

        business_process = CheckBusinessProcess(browser, browser.current_url)

        business_process.search()

        print('::-> ТЕСТ УСПЕШНО ПРОЙДЕН <-::')
        print("ВРЕМЯ ВЫПОЛНЕНИЯ::{:.3f}s".format(datetime.now().timestamp() - start_time))