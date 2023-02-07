from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import pyperclip

"""
    shopping.naver.com접속 -> 로그인 -> 로그인여부확인 -> top1 상품 접속하기
"""
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome = webdriver.Chrome("./chromedriver", options=options)
chrome.maximize_window() # 풀화면
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

id = input("아이디 : ")
pw = input("비밀번호 : ")

# ID값
# send_keys에 값을 직접 입력하면 캡차가 떠버리는데, 그것을 방지하기위헤 pyperclip을 사용
pyperclip.copy(id)
input_id.send_keys(Keys.CONTROL, "v")

# PW값
pyperclip.copy(pw)
input_pw.send_keys(Keys.CONTROL, "v")
input_pw.send_keys("\n")    # 엔터키

# 왜 로그아웃 element를 못찾는거지.?
# 함수내에서 visibility_of_element_located로 검색하는데, 실제로는 화면에 보여지지 않기에 찾지못함!
# presence_of_element_located로 바꿔주어야 함
logout_button = element_find_presence(short_wait, "#gnb_logout_button")

search = element_find_visibility(wait, "input[class^=_searchInput_search_input_]")
search.send_keys("이노스킨 탱크 케이스 아이폰11 프로 맥스")
time.sleep(0.5) # 바로 엔터치면 작동이 안할수도있다? 
search.send_keys("\n")

element_find_visibility(wait, "a[class^=basicList_link__]").click()

time.sleep(2)

# 크롬 탭 창을 switch 해줘야함!
# 이후에 상품탭에서 element를 찾지 못함!
# print(chrome.window_handles)
chrome.switch_to.window(chrome.window_handles[1])

element_find_visibility(wait, "a[aria-haspopup='listbox']")
# 선택값 가져오기
options = chrome.find_elements_by_css_selector("a[aria-haspopup='listbox']")

# 첫번째 선택값 세팅
options[0].click()
time.sleep(0.3)
# role=option 값이 많지만 아래와같이 코딩하면 첫번째 값을 세팅함.
# chrome.find_element_by_css_selector("ul[role='listbox'] a[role='option']").click()
chrome.find_elements_by_css_selector("ul[role='listbox'] a[role='option']")[0].click()

# 두번째 선택값 세팅
options[1].click()
time.sleep(0.3)
chrome.find_elements_by_css_selector("ul[role='listbox'] a[role='option']")[0].click()

# 구매하기 버튼 클릭
chrome.find_element_by_css_selector("div[class*='N=a:pcs.buy'] a").click()

# 결제하기 버튼 클릭!
element_find_visibility(wait, "button._doPayButton").click()

time.sleep(5)

chrome.quit() # 열린 크롬 전체를 꺼버린다. (모든 탭을 꺼버린다.)