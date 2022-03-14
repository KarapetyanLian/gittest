import selenium
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Firefox()
action = ActionChains(browser)
browser.maximize_window()

browser.get('https://www.amazon.com/')
search = browser.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
search.send_keys('netbook mini laptop')
searchBtt = browser.find_element_by_xpath('//*[@id="nav-search-submit-button"]').click()
sleep(2)
aser = browser.find_element_by_class_name('a-truncate-cut').click()
sleep(2)
add_to_card = browser.find_element_by_xpath('//*[@id="add-to-cart-button"]').click()
sleep(2)
btt = browser.find_element_by_xpath('//*[@id="attach-close_sideSheet-link"]').click()
sleep(2)
go_to_cart = browser.find_element_by_xpath('//*[@id="nav-cart"]').click()
sleep(2)
laptop_aspire = browser.find_element_by_class_name('a-truncate-cut').click()
sleep(3)
browser.close()
