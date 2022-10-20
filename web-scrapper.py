from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd

website = "https://www.thesun.co.uk/sport/football/"
path = "C:/<YOUR_PATH>/chromedriver_win32/chromedriver.exe"

# headless-mode
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)
titles = []
subtitles = []
links = []
containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

for container in containers:
    titles.append(container.find_element(by="xpath", value='./a/h2').text)
    subtitles.append(container.find_element(by="xpath", value='./a/p').text)
    links.append(container.find_element(by="xpath", value='./a').get_attribute("href"))

my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headlines-headless.csv')

driver.quit()
