from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

"""
    shopping.naver.com접속 -> 로그인
"""

# 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000") # 크롬 사이즈
options.add_argument("no-sandbox") # 탭 이동 불가기능(?)
# options.add_argument("headless") # 크롬창을 띄우지 않게

chrome = webdriver.Chrome("./chromedriver.exe", options=options) # 옵션값 적용
# chrome.get("https://naver.com")
chrome.get("https://shopping.naver.com")
# chrome.back() # 뒤로가기
# chrome.forward() # 앞으로가기
time.sleep(3)
# chrome.implicitly_wait(3) 3초 기다리기

# chreme 이란 브라우저에서 10초 동안 기다린다.
# input class가 _searchInput_search_text_3CUDs 요고인 친구가 떴을때까지?
# WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[class='_searchInput_search_text_3CUDs']")))
wait = WebDriverWait(chrome, 10)

# element가 뒤늦게 생성되는 친구들이 있기에, 왠만해선 wait을 사용하는게 나을듯?
# el = chrome.find_element_by_css_selector("input[class='_searchInput_search_text_3CUDs']") # 기다려주는 기능이 없음.

# el = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[class='_searchInput_search_text_3CUDs']"))) # 기다려주는 기능이 있음.

# 함수화
def find(wait, css_seletor):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_seletor)))

# search = find(wait, "input[class='_searchInput_search_text_3CUDs']")
search = find(wait, "._searchInput_search_text_3CUDs")
search.send_keys("아이폰 케이스")
# search.send_keys(Keys.RETURN) # 엔터키
# search.send_keys("아이폰 케이스\n") # 엔터키

button = find(wait, "._searchInput_button_search_1n1aw")
button.click()

time.sleep(3)


chrome.close()