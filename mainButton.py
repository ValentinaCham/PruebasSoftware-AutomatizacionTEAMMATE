import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

# Cargar .env
load_dotenv()
chromedriver_path = os.getenv("CHROMEDRIVER_PATH")

# Configurar Chrome en modo headless
options = Options()
options.add_argument("--headless")

# Iniciar navegador
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://arania-teammates.appspot.com/")
    time.sleep(2)

    # Buscar el <a> por su texto
    boton = driver.find_element(By.LINK_TEXT, "Request a Free Instructor Account")
    boton.click()
    time.sleep(2)

    nueva_url = driver.current_url
    print("✅ Redirigido a:", nueva_url)

finally:
    driver.quit()
