from selenium import webdriver

url= 'http://www.webscrapingfordatascience.com/complexjavascript'
driver = webdriver.Chrome('./chromedriver')
driver.get(url)

input('Press Enter to close the website')
driver.quit()

