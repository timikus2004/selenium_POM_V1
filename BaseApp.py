from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math, os


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        with open("text.txt", "r") as file:
            self.base_url = file.read()

        
    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self, *args):
        if args:
            return self.driver.get(args)
        else:
            return self.driver.get(self.base_url)

    def execute_window_open(self, *script):
        self.driver.execute_script("window.open(arguments[0],'_blank');", script)

    def get_window_handlers(self):
        return self.driver.window_handles

    def switch_to_window(self, window):
        self.driver.switch_to.window(window)

    def close(self):
        self.driver.close()

    def alert(self):
        self.driver.execute_script("alert('Robots at work');")

    def scroll(self, btn):
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", btn)

    def scroll_down(self, value):
        self.driver.execute_script("window.scrollBy(0, arguments[0]);", value)

    def confirm_to_alert(self):
        self.driver.switch_to.alert.accept()

    @staticmethod
    def calc_func(value):
        return math.log(abs(12 * math.sin(value)))/ math.log(10)
    
    @staticmethod
    def file_path(file):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(current_dir, file) 
