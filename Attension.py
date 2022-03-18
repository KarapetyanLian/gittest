import selenium
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
browser = webdriver.Firefox()
action = ActionChains(browser)
browser.implicitly_wait(10)
browser.maximize_window()
import unittest

class Test_Payment(unittest.TestCase):
 # browser.get('https://www.phptravels.net/signup')
 # browser.find_element_by_xpath('//*[@placeholder = "First Name"]').send_keys('Ani')
 # browser.find_element_by_xpath('//*[@placeholder =  "Last Name"]').send_keys('Avdalyan')
 # browser.find_element_by_xpath('//*[@placeholder = "Phone"]').send_keys('094633656')
 # browser.find_element_by_xpath('//*[@placeholder = "Email"]').send_keys('avdalyananul@mail.ru')
 # browser.find_element_by_xpath('//*[@placeholder = "Password"]').send_keys('123$456')
 # browser.find_element_by_xpath('//*[@type="submit"]').click()
 # browser.switch_to.window(browser.window_handles[1])
#
#  browser.get('https://www.phptravels.net/login')
#  browser.find_element_by_xpath('//*[@placeholder = "Email"]').send_keys('avdalyananul@mail.ru')
#  browser.find_element_by_xpath('//*[@placeholder = "Password"]').send_keys('123$456')
#  browser.find_element_by_xpath('//*[@type="submit"]').click()
#  browser.find_element_by_xpath('//a[@href = "https://www.phptravels.net/hotels"]').click()
#  sleep(3)
#  browser.find_element_by_xpath('//*[@id="select2-hotels_city-container"]').click()
#  browser.find_element_by_class_name('select2-search__field').send_keys("Yerevan")
#  browser.find_element_by_xpath('//*[text()= "Yerevan,Armenia"]').click()
#  browser.find_element_by_xpath('//*[@id="submit"]').click()
# # sleep(3)
#  browser.find_element_by_xpath('//a[@href="https://www.agoda.com/partners/partnersearch.aspx?cid=1743607&hid=299935&currency=USD&checkin=2022-03-21&checkout=2022-03-22&NumberofAdults=2&NumberofChildren=1&Rooms=1&pcs=6"]').click()
#  browser.switch_to.window(browser.window_handles[1])
#  browser.find_element_by_xpath('//*[@class="SearchboxBackdrop"]').click()
#  sleep(2)
#  browser.find_element_by_xpath('//*[text()="Select room"]').click()
#  sleep(2)
#  browser.find_element_by_xpath('//*[text()="Book now"]').click()
#  browser.find_element_by_xpath('//*[@id="firstName_lastName"]').send_keys("Ani Avdalyan")
#  browser.find_element_by_xpath('//*[@id="email"]').send_keys('avdalyananul@mail.ru')
#  sleep(2)
#  browser.find_element_by_xpath('//*[@id="retypeEmail"]').send_keys('avdalyananul@mail.ru')
#  sleep(2)
#  browser.find_element_by_xpath('//*[text()="NEXT: FINAL STEP"]').click()
#  sleep(5)
 browser.get('https://www.agoda.com/book/payment/')
 payment_page_title = browser.find_element_by_xpath('//*[@id="cc-form"]')
 strName = payment_page_title.text
 manual_version = "All card information is fully encrypted, secure and protected."


 def setUp(self):
    print('Test case started')

 def test_filter_Anhstakan(self):

    manual_vs = self.manual_version
    selenium_vs = self.strName
    assert manual_vs == selenium_vs


 def tearDown(self):
    print("End of the test case")

 if __name__ == "__main__":
       unittest.main()

 browser.close()



