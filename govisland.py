from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/Users/tristanpanora/Documents/chromedriver"

day = int(input("ENTER DAY: "))

day = day + 4

xpath = "//*[@id='ember574']/div[3]/div[4]/div[" + str(day) + "]"

driver = webdriver.Chrome(PATH)

driver.get("https://secure.rocket-rez.com/RocketWeb/?eid=8440d31434d050#/")

time.sleep(2)
element = driver.find_element_by_xpath("//*[@id='ember497']/div[3]/div[1]/div/div[2]/div")
element.click()

try:
    time.sleep(3) 
    element = driver.find_element_by_xpath(xpath)
    element.click()
except:
    time.sleep(6) 
    element = driver.find_element_by_xpath(xpath)
    element.click()

time.sleep(0.10)
element = driver.find_element_by_xpath("//*[@id='ember613']/div[6]/div/div[1]/div/div[2]")
element.click()

time.sleep(0.10)
element = driver.find_element_by_xpath("//*[@id='ember613']/div[9]")
element.click()

#WORKS!! ^^

close = int(input("Enter '1' to close: "))

if close == 1:
    driver.quit()

