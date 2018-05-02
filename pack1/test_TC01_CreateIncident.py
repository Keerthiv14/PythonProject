
from selenium import webdriver

 

browser =webdriver.Chrome()


def test_open_url():
    
    url='https://www.google.com/?safe=active&ssui=on'    
    browser.get(url)
    assert browser.current_url == url  


def test_close_browser():
    browser.close()
    browser.quit()