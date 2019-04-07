from selenium import webdriver
from pathlib import Path

def before_scenario(context, scenario):
    print("before scenario started")
    print(str(Path(__file__).parent.parent.absolute()) + "\drivers\chromedriver.exe")
    context.browser = webdriver.Chrome(str(Path(__file__).parent.parent.absolute()) + "\drivers\chromedriver.exe")
    context.browser.maximize_window()
    context.browser.implicitly_wait(20)

def after_scenario(context, scenario):
    context.browser = webdriver.quit()
