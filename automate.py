from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
# we are only importing webdriver from entire selenium

#loading particular driver of browser
#initializing web driver
Chorome_driver = webdriver.Chrome()

#opening a web url
Chorome_driver.get("https://rahulshettyacademy.com/angularpractice/")


#selenium can find find the elements by amany things like by name, class name or ID css selecter
Chorome_driver.find_element(By.NAME,"name").send_keys("ArchanaTest")
Chorome_driver.find_element(By.NAME,"email").send_keys("archana.sriniva@gmail.com")
Chorome_driver.find_element(By.ID,"exampleInputPassword1").send_keys("User123")
Chorome_driver.find_element(By.ID,"exampleCheck1").click()
#Selecting from dropdown
My_Choice = Select(Chorome_driver.find_element(By.ID, "exampleFormControlSelect1"))
#1st option
My_Choice.select_by_index(1)
#2nd option
#My_Choice.select_by_visible_text("Female")
#using css selecter for radio button
Chorome_driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
#using xpath for complex pattern matching
Chorome_driver.find_element(By.XPATH,"//input[@type='submit']").click()
#find the message data
message = Chorome_driver.find_element(By.CLASS_NAME, "alert-success").text


time.sleep(5)
#printing message
print(message)
assert "Success" in message
#Print title
print("Page Title : ", Chorome_driver.title)

#current url
print("page url : ", Chorome_driver.current_url)

#save screen shot
Chorome_driver.save_screenshot("pagehome1.png")
print("screen shot saved")

#Closing the driver /Stopping
Chorome_driver.quit()

