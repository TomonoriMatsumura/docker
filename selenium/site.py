from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from datetime import datetime

driver = webdriver.Remote(
command_executor='http://selenium-hub:4444/wd/hub',
desired_capabilities=DesiredCapabilities.CHROME)


prefix = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
extention = '.png'
filename = prefix + extention
path = '/tmp/png/'
file = path + filename

driver.get("http://qiita.com/reflet")
driver.save_screenshot(file)
driver.close()
driver.quit()
