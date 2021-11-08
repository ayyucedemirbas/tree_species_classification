#codes are from https://levelup.gitconnected.com/how-to-download-google-images-using-python-2021-82e69c637d59

#Imports Packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
#Opens up web driver and goes to Google Images
driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.google.ca/imghp?hl=en&tab=ri&authuser=0&ogbl')
box = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
box.send_keys('spruce tree')
box.send_keys(Keys.ENTER)
#Will keep scrolling down the webpage until it cannot scroll no more
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    try:
        driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
        time.sleep(2)
    except:
        pass
    if new_height == last_height:
        break
    last_height = new_height
    for i in range(1, 1000):
        try:
            driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot('dataset/spruce/('+str(i)+').png')
        except:
            pass
   


