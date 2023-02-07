from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

category = {
    "CPU" : "873",
    "메인보드" : "875",
    "메모리" : "874",
    "그래픽카드" : "876",
    "SSD" : "32617",
    "케이스" : "879",
    "파워" : "880",
}

category_css = {
    c : "dd.category_" + category[c] + " a" for c in category
}

options = webdriver.ChromeOptions()
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

def choose_one(text, options):
    print("------------")
    print(text)
    print("------------")
    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")
    choose = input("-> ")
    return int(choose) - 1

def parse_produts():
    time.sleep(2)
    products = []
    for p in finds_visible("div.scroll_box tr[class^=productList_]"):
        try:
            title = p.find_element_by_css_selector("p.subject a").text
            price = p.find_element_by_css_selector("span.prod_price").text
        except:
            continue

        products.append((title, price))
    return products
        
def go_to_category(category_name):
    find_visible(category_css[category_name]).click()
    time.sleep(1)

def choose_maker(text):
    options = finds_visible("input[name=makerCode]")
    i = choose_one(f"{text} 제조사를 선택해주세요.", [x.get_attribute("data") for x in options])
    options[i].find_element_by_xpath('..').click()
    return i

chrome.get("https://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=index&marketPlaceSeq=16")

#mainboard = find_visible("dd.category_" + category["메인보드"] + " a")
#mainboard = finds_visible("dd.category_875")
#mainboard.click()

# CPU 카테고리 클릭
go_to_category("CPU")

# CPU 제조사 불러오기
maker_idx = choose_maker("CPU")

# CPU 종류 불러오기
cpu_val = ""
mainboard_cpu_name = ""
if maker_idx == 0 :
    mainboard_cpu_name = "인텔 CPU용"
    cpu_val = "873|40|"
    graphic_card_val = "876|654|3518|"
    graphic_card_chipset = "876|658|"
elif maker_idx == 1 : 
    mainboard_cpu_name = "AMD CPU용"
    cpu_val = "873|312287|"
    graphic_card_val = "876|654|3517|"
    graphic_card_chipset = "876|657|"

options = finds_visible(f"input[value^='{cpu_val}']")
i = choose_one("CPU 종류를 선택해 주세요", [x.get_attribute("data") for x in options])
options[i].find_element_by_xpath('..').click()

cpus = parse_produts()


# 메인보드
go_to_category("메인보드")

# 메인보드 제조사 불러오기
choose_maker("메인보드")

# 메인보드 CPU 자동선택
time.sleep(1)
option = find_visible(f"input[data^='{mainboard_cpu_name}']")
option.find_element_by_xpath('..').click()

mainboards = parse_produts()

# 메모리
go_to_category("메모리")

# 메모리 제조사 불러오기
choose_maker("메모리")

# 데스크탑용 자동 선택
time.sleep(1)
options = finds_visible(f"input[data^='데스크탑용']")
options[0].find_element_by_xpath('..').click()

# DDR5 자동 선택
time.sleep(1)
options = finds_visible(f"input[data^='DDR5']")
options[0].find_element_by_xpath('..').click()

memories = parse_produts()


# 그래픽카드
go_to_category("그래픽카드")

# 그래픽카드 제조사 불러오기
choose_maker("그래픽카드")

# 그래픽카드 칩셋 제조사 자동선택
time.sleep(1)
option = find_visible(f"input[value^='{graphic_card_val}']")
option.find_element_by_xpath('..').click()

# 그래픽카드 칩셋 선택
options = finds_visible(f"input[value^='{graphic_card_chipset}']")
i = choose_one("CPU 종류를 선택해 주세요", [x.get_attribute("data") for x in options])
options[i].find_element_by_xpath('..').click()

graphics = parse_produts()

popular = {
    "cpu" : cpus[0],
    "mainboard" : mainboards[0],
    "memorie" : memories[0],
    "graphic" : graphics[0]
}

print("인기 1위 조합입니다.")
print("cpu")
print(popular["cpu"])
print("mainboard")
print(popular["mainboard"])
print("memorie")
print(popular["memorie"])
print("graphic")
print(popular["graphic"])

# 가성비 모델
def find_cheap(arr):
    cheap_idx = 0
    for i in range(len(arr)):
        cheap = arr[cheap_idx]
        a = arr[i]
        if int(a[1].replace(',', '')) < int(cheap[1].replace(',', '')):
            cheap_idx = i
    return arr[cheap_idx]

recommend = {
    "cpu" : find_cheap(cpus),
    "mainboard" : find_cheap(mainboards),
    "memorie" : find_cheap(memories),
    "graphic" : find_cheap(graphics)
}

print("가성비 조합입니다.")
print("cpu")
print(recommend["cpu"])
print("mainboard")
print(recommend["mainboard"])
print("memorie")
print(recommend["memorie"])
print("graphic")
print(recommend["graphic"])

time.sleep(10)
chrome.quit()