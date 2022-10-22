from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os
import sys

print("Starting the program...")
load_dotenv()
path = os.getenv('CHROME_DRIVER_PATH')
website = "https://www.thesun.co.uk/sport/football/"
#path = "C:/<YOUR_PATH>/chromedriver_win32/chromedriver.exe"

app_path = os.path.dirname(sys.executable)
now = datetime.now()
date_time = now.strftime("%Y-%m-%dT%H-%M-%S") 
 
# headless-mode
options = Options()
options.headless = True
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

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

file_name = f'headlines-{date_time}.csv'
full_path = os.path.join(app_path, file_name)

df_headlines.to_csv(file_name)

driver.quit()
print("Program Finished successfully")

