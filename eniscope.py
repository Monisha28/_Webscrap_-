from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions() 
options.add_experimental_option("prefs", {
  "download.default_directory": "/Users/moni/Downloads/eniscope",
  "download.prompt_for_download": False,
  "profile.default_content_setting_values.automatic_downloads": 1,
  "profile.default_content_settings.popups": 0,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True,
})
driver = webdriver.Chrome(executable_path='/Users/moni/Documents/webscrap/chromedriver',options=options)
driver.get("http://analytics.eniscope.com/login?go=%2F")

driver.find_element_by_name("username").send_keys("Chennai@ngp.co.uk")
driver.find_element_by_name("password").send_keys("Energy123")
loginbtn =driver.find_element_by_xpath("//button[@class='btn green uppercase'][@type='submit']").click()

ngp =driver.find_element_by_xpath("//a[@data-clientname='GAP Waste']")
driver.get(ngp.get_attribute("href"))
time.sleep(1)

field =driver.find_element_by_xpath("//div[@data-checkbox-parent='field-list'][text()='Select All']")
driver.execute_script("arguments[0].click();", field)

res = driver.find_element_by_xpath("//input[@id='res60'][@type='radio']")

driver.find_element_by_id("max-date-next").click()
time.sleep(2)
date = driver.find_element_by_id("max-date-range")
driver.execute_script("arguments[0].removeAttribute('readonly')", date)
date.clear()
date.send_keys("27 Aug 2019 - 27 Aug 2019")
time.sleep(1)

update = driver.find_element_by_xpath("//input[@id='submit']")

mainmenu = driver.find_element_by_xpath("//*[@id='actions']/div/a")

submenu =driver.find_element_by_xpath("//*[@id='actions']/div/ul/li[1]/a")

value = [50957,50958,50959,50963,50970,50972,50973,50960,50961,50962,50974,50964,50965,50966,50967,50968,50969,50971,53112,53113]

for v in value:
    s = "//input[@value='{}']".format(v)
    meter= driver.find_element_by_xpath(s)
    if(v==50957):
      driver.execute_script("arguments[0].click();", meter)
    driver.execute_script("arguments[0].click();", meter)
    driver.execute_script("arguments[0].click();", res)
    driver.execute_script("arguments[0].click();", update)
    time.sleep(2)
    driver.execute_script("arguments[0].click();", mainmenu)
    driver.execute_script("arguments[0].click();", submenu)
    time.sleep(3)
    driver.execute_script("arguments[0].click();", meter)

driver.close()



