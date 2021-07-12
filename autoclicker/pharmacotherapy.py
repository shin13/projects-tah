from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


chrome_path = "C:\\Python\\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

driver.get('http://59.120.129.104/taerm/index.jsp')

driver.find_element_by_name("uid").send_keys('YOUR-WORKER-ID')
driver.find_element_by_name("pwd").send_keys('YOUR-PASSWORD')
driver.find_element_by_xpath('/html/body/table/tbody/tr/td/form/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/a/img').click()
driver.implicitly_wait(30)

driver.find_element_by_xpath('//*[@id="Image39"]').click()
driver.implicitly_wait(30)
driver.find_element_by_xpath('//*[@id="mainContent"]/table[3]/tbody/tr[2]/td[2]/div[1]/table/tbody/tr[5]/td[1]/a').click()
driver.implicitly_wait(30)
driver.find_element_by_xpath('//*[@id="mainContent"]/table[1]/tbody/tr[2]/td[2]/div[1]/table/tbody/tr[1]/td[1]/a').click()
driver.implicitly_wait(30)
driver.find_element_by_xpath('//*[@id="fixed"]/table/tbody/tr[3]/td[2]/a').click()
driver.implicitly_wait(30)

window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
driver.implicitly_wait(30)

element = driver.find_elements_by_class_name("visitable")
link = element[0]
driver.execute_script("arguments[0].click();", link)
driver.implicitly_wait(300)

PDFs = driver.find_elements_by_link_text('PDF')
length = len(PDFs)
print(length) # Issue: print出來的數字沒有固定

#actions = ActionChains(driver)
for i in range(0,length):

    link = PDFs[i]

    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
    driver.implicitly_wait(30)
    window_before = driver.window_handles[1]
    driver.switch_to.window(window_before)
    driver.implicitly_wait(30)

driver.implicitly_wait(300)
driver.quit()

