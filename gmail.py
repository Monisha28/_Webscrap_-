import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


driver = webdriver.Chrome(executable_path='/Users/moni/Documents/chromedriver')
driver.get("http://mail.google.com")

time.sleep(2)

emailid=driver.find_element_by_id("identifierId")
emailid.send_keys("Your Emailid")

nextButton = driver.find_element_by_id("identifierNext")
nextButton.click()

time.sleep(2)

passw=driver.find_element_by_name("password")
passw.send_keys("Your Password")

nextButton = driver.find_element_by_id("passwordNext")
nextButton.click()

time.sleep(10)

soup = BeautifulSoup(driver.page_source, 'lxml')
mail = soup.find(id=':2z').find("email")
print(mail)


ele = driver.find_element_by_xpath("//div[@id=':2z']")
print(ele)
time.sleep(10)

# e = driver.find_element_by_xpath("//span[@data-hovercard-owner-id='127']")
# print(e)

# time.sleep(10)

# sentbtn = driver.find_element_by_id(":kc")
# sentbtn.click()

# time.sleep(6)

# mail = driver.find_element_by_id(":p6")
# mail.click()

# time.sleep(10)

# content= driver.find_element_by_id(":156").text
# print (content)
# soup = BeautifulSoup(driver.page_source, 'lxml')



# # page = driver.page_source
# # soup = BeautifulSoup(page, 'lxml')
# # print (soup.prettify())
# content =  soup.find_all('div',id=':156')
# # print(content)

# for i in content:
#     print(i.get_text())
#                 # words = i.get_text()
#                 # print(words)
# driver.quit()
# # time.sleep(10)


# driver.switch_to_frame('canvas_frame')


# sentmail= driver.find_element_by_link_text('Sent Mail')
# sentmail.click()


# time.sleep(10)


# sentmail= driver.find_element_by_link_text('Your Name')
# sentmail.click()


# lout= driver.find_element_by_link_text('Sign out')
# lout.click()