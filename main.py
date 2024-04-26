
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://demoqa.com/")


elements_block = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[1]")
elements_block.click()



text_box_option = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div[1]/div/ul/li[1]")
text_box_option.click()

input_values = ["GERES", "fgg@eg.com", "eah", "hte"]


text_box1 = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[1]/div[2]/input')
text_box1.clear()
text_box1.send_keys(input_values[0])

text_box2 = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[2]/div[2]/input')
text_box2.clear()
text_box2.send_keys(input_values[1])

text_box3 = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[3]/div[2]/textarea')
text_box3.clear()
text_box3.send_keys(input_values[2])

text_box4 = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[4]/div[2]/textarea')
text_box4.clear()
text_box4.send_keys(input_values[3])


sub_button = driver.find_element(By.ID, 'submit')
driver.execute_script("arguments[0].click();", sub_button)
#sub_button.click()
time.sleep(8)
name = driver.find_element(By.ID, 'name')
output_values = driver.find_elements(By.XPATH,"//p[@id='output']")

result_values = driver.find_elements(By.XPATH,"//p[@id='output']")
for i in range(len(result_values)):
    assert result_values[i].text == input_values[i]
