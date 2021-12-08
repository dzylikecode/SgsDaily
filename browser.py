from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

from config import *

__all__ = ['OpenGame', 'QuitGame']

def OpenGame(url, username, password):

    # 打开Google
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # 搜索网址
    driver.get(url)
    # 获取网页标题
    title = driver.title
    # 根据 html 元素 `class=dobest_input` 获取对象
    username_input, password_input = driver.find_elements(By.CLASS_NAME, 'dobest_input')
    # 填入相应的
    username_input.send_keys(username)
    password_input.send_keys(password)
    # 点击相应的东西
    driver.find_element(By.CLASS_NAME, 'mycheckbox').click()
    driver.find_element(By.CLASS_NAME, 'dobest_de_btn').click()
    time.sleep(operation_interval)
    # The :nth-child(n) selector matches every element 
    # that is the nth child, regardless of type, of its parent
    driver.find_element(By.CSS_SELECTOR, '.new_ser1:nth-child(2)').click()
    # 登录对应的是 id
    driver.find_element(By.ID, "newGoInGame").click()
    time.sleep(page_load_interval)
    return driver, title

def QuitGame(driver):
    driver.quit()
