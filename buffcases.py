from lxml import html
from selenium import webdriver
import requests
import time

url = "https://www.buffalo.edu/coronavirus/health-and-safety/covid-19-dashboard.html"
page = requests.get(url)
tree = html.fromstring(page.content)

covidCases = tree.xpath('/html/body/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[10]/div[1]/div[1]/div/table/tbody/tr[9]/th[2]/b/i/text()') #HAVE TO ADD '/text()' to the end to get the text.

updateTime = tree.xpath('//*[@id="title_1840522633"]/text()')


print("TOTAL BUFF CASES: ", covidCases)
print("TIME UPDATED: ", updateTime)
