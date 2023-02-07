from selenium import webdriver
from selenium_stealth import stealth
import time

chrome = webdriver.Chrome("./chromedriver")

url = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"

chrome.get(url)

stealth(
    chrome,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,

)

time.sleep(5)
chrome.quit()