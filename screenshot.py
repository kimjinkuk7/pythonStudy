from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

options = webdriver.ChromeOptions()
# 브라우저를 띄우지 않는 옵션
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome = webdriver.Chrome("./chromedriver", options=options)
wait = WebDriverWait(chrome, 10)
    
def find_present(css_element):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_element)))

def finds_present(css):
    find_present(css)
    return chrome.find_elements_by_css_selector(css)

def find_visible(css_element):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_element)))

def finds_visible(css):
    find_visible(css)
    return chrome.find_elements_by_css_selector(css)

chrome.get("https://www.naver.com/")

find_visible("input#query").send_keys("패스트캠퍼스\n")

find_visible("li.menu a[href^='?where=view']").click()

e = find_visible("li[data-cr-rank='3']")
chrome.execute_script(
    """
    document.querySelector("li[data-cr-rank='3']").setAttribute('style', 'border:10px solid red')
    """
    )

# 특정 element 만 스크린샷 찍기
e.screenshot("./test.png")

chrome.set_window_size(1000, 10000)
chrome.save_screenshot("./test2.png")

body = find_visible("body")
body.screenshot("./test3.png")

chrome.quit()