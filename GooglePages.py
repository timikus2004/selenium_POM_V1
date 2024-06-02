from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class GoogleSeacrhLocators:
    LOCATOR_GOOGLE_SEARCH_FIELD = (By.CLASS_NAME, 'gLFyf')
    LOCATOR_GOOGLE_SEARCH_DATA = (By.CSS_SELECTOR, "[class='sbct']")
    LOCATOR_HREF = (By.PARTIAL_LINK_TEXT, 'pochta')
    LOCATOR_TITLE = (By.TAG_NAME, 'title')
    LOCATOR_SELECT = (By.TAG_NAME, "select")
    LOCATOR_CHOOSE_OPTION = (By.CSS_SELECTOR, "select > option:nth-child(2)")
    LOCATOR_SPANS_TO_CNT_SUM = (By.CSS_SELECTOR, ".nowrap")
    LOCATOR_BUTTON = (By.TAG_NAME, "button")
    LOCATOR_X_VALUE = (By.CSS_SELECTOR, "[id='input_value']")
    LOCATOR_INPUT = (By.CSS_SELECTOR, "[id='answer']")
    LOCATOR_CHECKBOX = (By.CSS_SELECTOR, "[id='robotCheckbox']")
    LOCATOR_RADIO = (By.CSS_SELECTOR, "[id='robotsRule']")

class GoogleSearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(GoogleSeacrhLocators.LOCATOR_GOOGLE_SEARCH_FIELD)
        search_field.send_keys(word)
        return search_field

    def get_list(self):  
        elems = self.find_elements(GoogleSeacrhLocators.LOCATOR_GOOGLE_SEARCH_DATA,time=2)
        #txtbox_elms = [x.text for x in elems if len(x.text) > 1]
        return len(elems)

    def click_input(self):
        self.find_elements(GoogleSeacrhLocators.LOCATOR_GOOGLE_SEARCH_DATA)[0].click()
        
    def get_new_site_url(self):
        return self.find_element(GoogleSeacrhLocators.LOCATOR_HREF).get_attribute("href")

    def get_title(self):
        return self.find_element(GoogleSeacrhLocators.LOCATOR_TITLE).text

    def click_select(self):
        self.find_element(GoogleSeacrhLocators.LOCATOR_SELECT).click()
    
    def choose_option(self):
        a =  self.find_element(GoogleSeacrhLocators.LOCATOR_CHOOSE_OPTION).text
        b =  self.find_element(GoogleSeacrhLocators.LOCATOR_CHOOSE_OPTION).get_attribute("value")
        return a, b

    def click_select(self, value: str):
        select =  Select(self.find_element(GoogleSeacrhLocators.LOCATOR_SELECT))
        select.select_by_value(value)
    
    def get_numbers(self):
        elms =  self.find_elements(GoogleSeacrhLocators.LOCATOR_SPANS_TO_CNT_SUM)
        numbers = [int(x.text) for x in elms if x.text.isdigit()]
        summ_ = 0
        for x in numbers:
            summ_ += x
        return summ_
    
    def click_btn(self):
        self.find_element(GoogleSeacrhLocators.LOCATOR_BUTTON).submit()
    
    def get_btn_elem(self):
        return self.find_element(GoogleSeacrhLocators.LOCATOR_BUTTON)

    def get_x_value(self):
        return self.find_element(GoogleSeacrhLocators.LOCATOR_X_VALUE).text

    def enter_values(self, value):
        self.find_element(GoogleSeacrhLocators.LOCATOR_INPUT).send_keys(value)

    def click_checkbox(self):
        self.find_element(GoogleSeacrhLocators.LOCATOR_CHECKBOX).click()
    
    def click_radio_input(self):
        self.find_element(GoogleSeacrhLocators.LOCATOR_RADIO).click()
