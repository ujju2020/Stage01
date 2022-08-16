import time
from selenium import webdriver
import self
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("D:\OneDrive - Indian Cable Net Co. Ltd\Desktop\Selenium\chromedriver_win32\chromedriver.exe")
driver.get("https://d3p9d8t4dp35oz.cloudfront.net/#/login")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.find_element(By.ID,"userName").send_keys("subhrajyoti.pramanik@siti.esselgroup.com")
driver.find_element(By.ID,"password").send_keys("BumbleB33*2021")
driver.find_element(By.ID,"loginButton").click()
time.sleep(2)
driver.switch_to("https://d3p9d8t4dp35oz.cloudfront.net/#/subscription/client_users/users")
#driver.find_element(By.ID,"RMNID").send_keys("9830283204")
#driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/main/div/div/div[1]/div/div[4]/div[1]/button/span[1]").click()

time.sleep(3)
driver.close()
#driver.quit()


