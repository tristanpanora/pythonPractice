from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/Users/tristanpanora/Documents/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://www.govisland.com/visit-the-island/ferry")

search = driver.find_element_by_name("q") #q is the name of the search bar

search.send_keys("events")
search.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()




 




















#id in html is guarenteed to be unique
