import sys
import os 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv

load_dotenv()

my_dir=sys.argv[1]

parent_dir_path = os.getenv("FILEPATH")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")


#print("you successfully passed as an argument the name of the the directory", my_dir)
#parent_dir_path="/Users/adinaciubancan/Documents/MyProjects"
my_dir_path=os.path.join(parent_dir_path, my_dir)

driver=webdriver.Chrome("/Users/adinaciubancan/Documents/chromedriver 2")
driver.get("https://github.com/login")
driver.maximize_window()


def makeproject():
  
   os.mkdir(my_dir_path) #or makedirs?
  
   #selenium press button
   
   
   user=driver.find_element_by_xpath('//*[@id="login_field"]')
   #button=browser.find_element_by_css_selector('login_field')
   user.send_keys("", username)

   passw=driver.find_element_by_xpath('//*[@id="password"]')
   passw.send_keys("", password)

   signin=driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]')
   signin.click()

   driver.get("https://github.com/new")
   
   newrep=driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input')
   newrep.send_keys("",my_dir)

   signin=driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/div[2]/label/input')
   signin.click()

   signin=driver.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button')
   signin.submit()

   print("Succesfully created repository {}".format(my_dir))

   time.sleep(5)
   driver.close()
if __name__ == "__main__":
    makeproject()
