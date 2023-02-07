from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import pyperclip

"""
    shopping.naver.com접속 -> 로그인 -> 로그인여부확인 -> 리스트 무한스크롤 -> title 가져오기
"""

chrome = webdriver.Chrome("./chromedriver.exe")
wait = WebDriverWait(chrome, 10)
short_wait = WebDriverWait(chrome, 3)

chrome.get("https://shopping.naver.com")

# 생성된 element확인 후 클릭 (그려지는게 조금 늦어질때는 동작안할 수 있음.)
# login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button"))).click()

# 중복된 코드 함수화
def element_find_visibility(wait, css_element):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_element)))
    
def element_find_presence(wait, css_element):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_element)))

# 생성된 element가 잘 그려져 있는지 확인 후 클릭
# login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button"))).click()

# input_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#id")))
# input_pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#pw")))

login_button = element_find_visibility(wait, "a#gnb_login_button").click()
input_id = element_find_visibility(wait, "input#id")
input_pw = element_find_visibility(wait, "input#pw")

# send_keys에 값을 직접 입력하면 캡차가 떠버리는데, 그것을 방지하기위헤 pyperclip을 사용
pyperclip.copy("kimjinkuk7")
# input_id.send_keys("kimjinkuk7")
input_id.send_keys(Keys.CONTROL, "v")
pyperclip.copy("xhdtls12!@")
# input_pw.send_keys("xhdtls12!@")
input_pw.send_keys(Keys.CONTROL, "v")
input_pw.send_keys("\n")    # 엔터키

# 왜 로그아웃 element를 못찾는거지.?
# 함수내에서 visibility_of_element_located로 검색하는데, 실제로는 화면에 보여지지 않기에 찾지못함!
# presence_of_element_located로 바꿔주어야 함
logout_button = element_find_presence(short_wait, "#gnb_logout_button")

search = element_find_visibility(wait, "input._searchInput_search_text_3CUDs")
search.send_keys("아이폰 케이스")
time.sleep(0.5) # 바로 엔터치면 작동이 안할수도있다? 
search.send_keys("\n")

element_find_visibility(wait, "div[class^=basicList_info_area__]")

# 스크롤
for i in range(8):
    chrome.execute_script("window.scrollBy(0, " + str(i*1000) + ")")
    time.sleep(0.5)

items = chrome.find_elements_by_css_selector("div[class^=basicList_info_area__]")

for item in items:
    # 광고제거
    try :
        item.find_element_by_css_selector("button[class^=ab_]")
        continue
    except :
        pass
    
    print(item.find_element_by_css_selector("a[class^=basicList_link__]").text)

time.sleep(3)

chrome.close()