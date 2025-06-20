import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

load_dotenv()

def get_driver():
    chromedriver_path = os.getenv("CHROMEDRIVER_PATH")
    options = Options()
    options.add_argument("--headless")
    return webdriver.Chrome(service=Service(chromedriver_path), options=options)
