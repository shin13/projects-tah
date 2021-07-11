from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver import ActionChains
# from bs4 import BeautifulSoup

chrome_path = "C:\\Python\\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

driver.get('http://59.120.129.104/taerm/index.jsp')

driver.find_element_by_name("uid").send_keys('152551')
driver.find_element_by_name("pwd").send_keys('Ab!@34567')

#driver.switch_to_window(window_after)
driver.find_element_by_xpath('/html/body/table/tbody/tr/td/form/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/a/img').click()
#driver.execute_script("window.open()")
driver.implicitly_wait(30)

#driver.execute_script('window.open(url)')
#driver.current_window_handle

  #獲得當前瀏覽器所有視窗
#print(len(windows))
#driver.switch_to.window(windows[0]) #切換到最新開啟視窗（注：也就是全部課程這個視窗）
#current_window = driver.current_window_handle

#first_window = driver.window_handles[0]
#second_window = driver.window_handles[1]
#driver.switch_to_window(second_window)

driver.find_element_by_xpath('//*[@id="Image39"]').click()
driver.find_element_by_xpath('//*[@id="mainContent"]/table[3]/tbody/tr[2]/td[2]/div[1]/table/tbody/tr[5]/td[1]/a').click()
driver.find_element_by_xpath('//*[@id="mainContent"]/table[1]/tbody/tr[2]/td[2]/div[1]/table/tbody/tr[1]/td[1]/a').click()
driver.find_element_by_xpath('//*[@id="fixed"]/table/tbody/tr[2]/td[2]/a').click()
driver.implicitly_wait(30)

window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
# driver.find_element_by_id("details-button").click()
# driver.find_element_by_id("proceed-link").click()
driver.implicitly_wait(30)

element = driver.find_element_by_link_text('Current Issue')
driver.execute_script("arguments[0].click();", element)
driver.implicitly_wait(300)
#<a href="/toc/aopd/current" data-item-name="view-current-issue">Current Issue</a>

#print(driver.page_source)
a = driver.find_elements_by_css_selector('[alt="PDF Download"]')

length = len(a)
print (length)
links = a

for i in range(0,length):
    link = links[i]
    driver.execute_script("arguments[0].click();", link)
#    actions = ActionChains(driver)
#    link.click()
    driver.implicitly_wait(30)
    window_before = driver.window_handles[1]
    driver.switch_to.window(window_before)
    driver.implicitly_wait(30)

driver.implicitly_wait(300)
driver.quit()
