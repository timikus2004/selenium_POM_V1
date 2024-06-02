from GooglePages import GoogleSearchHelper
from StepikPages import StepikPages
import time


'''
def test_go_toPage(browser):

    my_driver = GoogleSearchHelper(browser)
    my_driver.go_to_site()
    #assert my_driver.get_title() == 'Новая вкладка'

    my_driver.enter_word("Почта РФ")
    time.sleep(1)

    my_driver.click_input()
    url_data = my_driver.get_new_site_url()
    assert url_data == 'https://www.pochta.ru/'

    my_driver.execute_window_open(str(url_data))
    time.sleep(3)
    my_driver.close()


def test_cnt_elems(browser): 
    my_driver = GoogleSearchHelper(browser)
    my_driver.go_to_site()
    time.sleep(1)
    summ_= my_driver.get_numbers()
    my_driver.click_select(str(summ_))
    time.sleep(1)
    my_driver.click_btn()
    time.sleep(3)
'''
       
def test_alert(browser):
    driver = StepikPages(browser)
    driver.go_to_site()
    this_window = driver.get_window_handlers()[0]
    time.sleep(4)
    driver.submit_form()
    new_window = driver.get_window_handlers()[1]
    driver.switch_to_window(new_window)
    time.sleep(3)

