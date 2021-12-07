from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from src.pages.base_page import BasePage
from src.locators.locators import ExitLocators, RegistrationLocators, EntranceLocators, SearchLocators
import time
import random

class CheckBusinessProcess(BasePage):
    def registration(self):
        click_on_entrance = self.browser.find_element(*RegistrationLocators.REG_ENTRANCE)
        click_on_entrance.click()

        click_on_registration = self.browser.find_element(*RegistrationLocators.REG_REGISTRATION)
        click_on_registration.click()

        input_first_name = self.browser.find_element(*RegistrationLocators.REG_FIRST_NAME)
        input_first_name.send_keys('Борис')
        input_first_name.send_keys(Keys.ENTER)

        # ИСПОЛЬЗОВАЛ ОДНОРАЗОВЫЙ --EMAIL-- 
        input_email = self.browser.find_element(*RegistrationLocators.REG_EMAIL)
        input_email.send_keys('b2cc337bb0@emailnax.com')
        input_first_name.send_keys(Keys.ENTER)

        input_passwd = self.browser.find_element(*RegistrationLocators.REG_PASSWD)
        rnd = random.randint(10000000, 99999999)
        print(rnd)
        input_passwd.send_keys(rnd)
        input_first_name.send_keys(Keys.ENTER)

        button_submit = self.browser.find_element(*RegistrationLocators.REG_SUBMIT)
        button_submit.click()
        
        time.sleep(5)

        welcome = self.browser.find_element(*RegistrationLocators.REG_ASSERT)
        print(welcome.text)

        assert "ДОБРО ПОЖАЛОВАТЬ!" in welcome.text
    
    def entrance(self):
        click_on_entrance = self.browser.find_element(*RegistrationLocators.REG_ENTRANCE)
        click_on_entrance.click()

        input_login = self.browser.find_element(*EntranceLocators.ENTR_LOGIN)
        input_login.send_keys('b2cc337bb0@emailnax.com')

        input_passwd = self.browser.find_element(*EntranceLocators.ENTR_PASSWD)
        input_passwd.send_keys('44670711')

        button_submit = self.browser.find_element(*EntranceLocators.ENTR_SUBMIT)
        button_submit.click()

        time.sleep(3)
        click_on_entrance = self.browser.find_element(*RegistrationLocators.REG_ENTRANCE)
        print(click_on_entrance.text)
        assert click_on_entrance.text != "Войти"

    def exit(self):
        hover = ActionChains(self.browser).move_to_element(self.browser.find_element(By.XPATH,'//*[@data-qa="account-link"]'))
        hover.perform()

        click_on_exit = self.browser.find_element(*ExitLocators.EX_EXIT)
        click_on_exit.click()

    def search(self):

        self.entrance()

        input_search = self.browser.find_element(*SearchLocators.SRCH_INPUT)
        input_search.send_keys("худи")
        input_search.send_keys(Keys.ENTER)

        select_man = self.browser.find_element(*SearchLocators.SRCH_SELECT_MAN)
        select_man.click()

        click_on_sort_menu = self.browser.find_element(*SearchLocators.SRCH_OPEN_SORT_MENU)
        click_on_sort_menu.click()

        click_on_high_to_low_price = self.browser.find_element(*SearchLocators.SRCH_SORT)
        click_on_high_to_low_price.click()

        click_on_size_menu = self.browser.find_element(*SearchLocators.SRCH_OPEN_SIZE_MENU)
        click_on_size_menu.click()

        click_on_clothes_menu = self.browser.find_element(*SearchLocators.SRCH_OPEN_CLOTHES_MENU)
        click_on_clothes_menu.click()

        select_size_xxl = self.browser.find_element(*SearchLocators.SRCH_SELECT_SIZE_XXL)
        select_size_xxl.click()

        apply_select_size = self.browser.find_element(*SearchLocators.SRCH_APPLY_SELECT_SIZE)
        apply_select_size.click()

        select_item = self.browser.find_element(*SearchLocators.SRCH_SELECT_ITEM)
        select_item.click()

        click_on_size = self.browser.find_element(*SearchLocators.SRCH_CLICK_ON_SIZE)
        
        bg = self.browser.find_element(By.CSS_SELECTOR, 'body')
        bg.send_keys(Keys.SPACE)
        time.sleep(1)
        click_on_size.click()

        click_on_add_to_basket = self.browser.find_element(*SearchLocators.SRCH_ADD_TO_BASKET)
        click_on_add_to_basket.click()

        go_to_basket = self.browser.find_element(*SearchLocators.SRCH_GO_TO_BASKET)
        go_to_basket.click()

        try:
            checkout = self.browser.find_element(*SearchLocators.SRCH_CHECKOUT)
            checkout.click()
        except:
            pass

        checkout_confirm = self.browser.find_element(*SearchLocators.SRCH_CHECKOUT_CONFIRM)
        checkout_confirm.click()

        error_message = self.browser.find_element(*SearchLocators.SRCH_ERROR_MESSAGE).text
        print(error_message)
        
        assert error_message == "Заполните свои данные, выберите тип доставки и оплаты, чтобы продолжить."

        time.sleep(5)



