from selenium import webdriver
from selenium.webdriver.common.by import By


url = "https://masina-de-gaurit-si-insurubat.compari.ro/evotools/676028-p552390993/"

driver = webdriver.Chrome()
driver.get("https://masina-de-gaurit-si-insurubat.compari.ro/evotools/676028-p552390993/")

price = driver.find_element(By.CLASS_NAME, "visible-xs").text
print(price)
