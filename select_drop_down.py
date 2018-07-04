from selenium import webdriver;
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

#webdriver driver = new ChromeDriver()
browser= webdriver.Chrome();
browser.get('file:///S:/Summer\'18/Study/html_code_03_02.html');
#user_id = browser.find_element_by_id('q')

select =Select(browser.find_element_by_name('numReturnSelect'))
select.select_by_index(4)
time.sleep(3)

select.select_by_visible_text("200")
time.sleep(3)

select.select_by_value("250")
time.sleep(3)


submit_button = browser.find_element_by_name("continue")
submit_button.submit()
#user_name.send_keys("pycon")
#user_name.send_keys(Keys.RETURN)

#time.sleep(3)
browser.close()