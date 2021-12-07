from selenium.webdriver.common.by import By

class RegistrationLocators():
    REG_ENTRANCE = (By.XPATH, '//*[@data-qa="account-link"]')
    REG_REGISTRATION = (By.XPATH, '//div[contains(text(), "регистрация")]')
    REG_FIRST_NAME = (By.XPATH, '//input[@name="firstName"]')
    REG_EMAIL = (By.XPATH, '//input[@data-qa="regEmail"]')
    REG_PASSWD = (By.XPATH, '//input[@data-qa="regPassword"]')
    REG_SUBMIT = (By.XPATH, '//button[@data-qa="regSubmitBtn"]')
    REG_ASSERT = (By.XPATH, '//div[@class="padding-24 caption--center"]/p[1]')

class EntranceLocators():
    ENTR_LOGIN = (By.XPATH, '//input[@data-qa="loginEmail"]')
    ENTR_PASSWD = (By.XPATH, '//input[@data-qa="loginPassword"]')
    ENTR_SUBMIT = (By.XPATH, '//button[@data-qa="loginSubmit"]')

class ExitLocators():
    EX_EXIT = (By.XPATH, '//a[text()="Выйти"]')

class SearchLocators():
    SRCH_INPUT = (By.XPATH, '//input[@class="search-field__input js-site-search-input"]')
    SRCH_SELECT_MAN = (By.XPATH, '//ul[@class="filter-menu__content"]/li[2]/a')
    SRCH_OPEN_SORT_MENU = (By.XPATH, '//div[@class="check-dropdown-list js-facet-element js-filter-element active show"]')
    SRCH_SORT = (By.XPATH, '//div[@class="check-dropdown-list__list check-dropdown-list__list--mobile-padding-20 d-flex flex-column custom-scroll"]/label[2]/a')
    SRCH_OPEN_SIZE_MENU = (By.XPATH, '//div[@data-qa="productSizeGroupsFacet"]')
    SRCH_OPEN_CLOTHES_MENU = (By.XPATH, '//div[@data-group-name="Одежда"]')
    SRCH_SELECT_SIZE_XXL = (By.XPATH, '//label[@data-qa="facet_XXL;Одежда"]')
    SRCH_APPLY_SELECT_SIZE = (By.XPATH, '//p[@data-qa="apply_productSizeGroupsFacet"]')
    SRCH_SELECT_ITEM = (By.XPATH, '//div[@data-listing-type="mainListing"]/div[5]')
    SRCH_CLICK_ON_SIZE = (By.XPATH, '/html/body/div[7]/main/div[3]/div/div[2]/div[1]/div/div[6]/div[3]/div[6]/div')
    SRCH_ADD_TO_BASKET = (By.XPATH, '//button[@data-add-in-basket="Добавить в корзину"]')
    SRCH_GO_TO_BASKET = (By.XPATH, '//a[@class="pop-up-basket__buttons-basket uk-button uk-button--red"]')
    SRCH_CHECKOUT = (By.XPATH, '//a[@class="press-button press-button--red-style press-button--folow-mobile js-order-checkout-button js-dataLayer-card"]')
    SRCH_CHECKOUT_CONFIRM = (By.XPATH, '//*[@data-type="big"]')
    SRCH_ERROR_MESSAGE = (By.XPATH, '//span[@class="js-checkout-error-message-content"]')