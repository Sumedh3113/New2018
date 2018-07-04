"""
Automated Code to drag and drop the elements on web page
"""

from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("http://jqueryui.com/droppable")
driver.switch_to.frame(0)
action = ActionChains(driver)

source = driver.find_element_by_id("draggable")
destination = driver.find_element_by_id("droppable")

action.drag_and_drop_by_offset(source,100,100).perform()
time.sleep(2)

action.drag_and_drop(source,destination).perform()
time.sleep(5)

driver.close()