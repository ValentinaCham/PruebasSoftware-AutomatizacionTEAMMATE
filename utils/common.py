# utils/common.py

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
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

def login_como_instructor(driver):
    try:
        # Ir directamente al login de Google para instructores
        driver.get("https://arania-teammates.appspot.com//login?nextUrl=https://arania-teammates.appspot.com//web/instructor/home")
        
        print("🔐 Se abrió la página de login de Google para instructores.")
        print("🕒 Tienes 60 segundos para completar el login manualmente...")

        time.sleep(60)  # Esperar que completes OAuth2 manualmente

        # Validar que se redirigió correctamente
        if "web/instructor/home" in driver.current_url:
            print("✅ Login exitoso, ya estás en el panel del instructor.")
            return True
        else:
            print(f"⚠️ No se llegó al panel esperado. URL actual: {driver.current_url}")
            return False

    except Exception as e:
        print(f"❌ Error durante el login: {str(e)}")
        return False