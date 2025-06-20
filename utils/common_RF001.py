# utils/common.py

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def abrir_formulario_registro(driver):
    try:
        driver.get("https://arania-teammates.appspot.com/")
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "Request a Free Instructor Account").click()
        time.sleep(2)
        driver.find_element(By.ID, "btn-am-instructor").click()
        time.sleep(2)
        return True
    except NoSuchElementException as e:
        print(f"❌ No se pudo acceder al formulario: {str(e)}")
        return False