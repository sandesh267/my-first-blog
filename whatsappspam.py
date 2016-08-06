from selenium import webdriver
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver')
driver.get('http://web.whatsapp.com')
input()
elem = driver.find_element_by_xpath('//span[contains(text(),"Gautam Reddy")]')
elem.click()
elem1 = driver.find_elements_by_class_name('input')
a = 0
while True:
	elem1[1].send_keys('Your whatsapp is hacked')
	b.find_element_by_class_name('send-container').click()
