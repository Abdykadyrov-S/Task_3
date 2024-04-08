from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from random import shuffle


driver = webdriver.Chrome()

driver.get("https://room-number.ru/category/thailand/")

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "entry-title")))

# headlines = driver.find_elements_by_css_selector(".entry-title.td-module-title a")
headlines = driver.find_elements(By.CSS_SELECTOR, ".entry-title, .entry-title a")
descriptions = driver.find_elements(By.CSS_SELECTOR, ".entry-content p")

headlines_spisok = []
descriptions_spisok = []


for description in descriptions:
    descriptions_spisok.append(description.text)
    # print(number, desc.text)        
while "" in descriptions_spisok:
    descriptions_spisok.remove("")

unique_list_descriptions = list(set(descriptions_spisok))
# print(unique_list_descriptions)

print("\n\n\n\n\n\n\n\n\n\n\n\ntest\n\n\n\n\n\n")
for headline in headlines:
    headlines_spisok.append(headline.text)
    # print(number, headline.text)        
while "" in headlines_spisok:
    headlines_spisok.remove("")

unique_list_headlines = list(set(headlines_spisok))
print(unique_list_headlines)
# print(headlines_spisok)


driver.quit()
