from BaseApp import BasePage
from selenium.webdriver.common.by import By



class StepikLocators():
    LOCATOR_FIRST_NAME = (By.NAME, "firstname")
    LOCATOR_LAST_NAME = (By.NAME, "lastname")
    LOCATOR_EMAIL = (By.NAME, "email")
    LOCATOR_FILE_UPLOAD = (By.NAME, "file")
    LOCATOR_SUBMIT = (By.TAG_NAME, "button")
    LOCATOR_X_VALUE = (By.CSS_SELECTOR, "[id='input_value']")
    LOCATOR_INPUT = (By.CSS_SELECTOR, "[id='answer']")

class StepikPages(BasePage):
    def enter_first_name(self):
        self.find_element(StepikLocators.LOCATOR_FIRST_NAME).send_keys("Timur")

    def enter_last_name(self):
        self.find_element(StepikLocators.LOCATOR_LAST_NAME).send_keys("ZInnatullin")

    def enter_email(self):
        self.find_element(StepikLocators.LOCATOR_EMAIL).send_keys("timikus2004@yandex.ru")

    def upload_file(self, path):

        self.find_element(StepikLocators.LOCATOR_FILE_UPLOAD).send_keys(path)

    def submit_form(self):
        self.find_element(StepikLocators.LOCATOR_SUBMIT).submit()

    def button_click(self):
        self.find_element(StepikLocators.LOCATOR_SUBMIT).click()

    def get_x_value(self):
        return self.find_element(StepikLocators.LOCATOR_X_VALUE).text

    def enter_values(self, value):
        self.find_element(StepikLocators.LOCATOR_INPUT).send_keys(value)