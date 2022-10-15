from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.thesun.co.uk/sport/football/"
path = "C:/Users/sebas/chromedriver_win32/chromedriver.exe"

#service = Service(executable_path=r"C:/Users/sebas/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(executable_path=r"C:/Users/sebas/chromedriver_win32/chromedriver.exe")
driver.get(website)