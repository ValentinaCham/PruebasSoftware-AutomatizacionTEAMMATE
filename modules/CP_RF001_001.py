from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.common import abrir_formulario_registro

def run(driver):
    if not abrir_formulario_registro(driver):
        return "❌ Error al abrir el formulario."

    try:
        driver.find_element(By.ID, "name").send_keys("Valentina Chambi")
        driver.find_element(By.ID, "institution").send_keys("Universidad Nacional de Colombia")
        driver.find_element(By.ID, "country").send_keys("Colombia")
        driver.find_element(By.ID, "email").send_keys("vchambilla@universidad.edu.co")
        driver.find_element(By.ID, "comments").send_keys("")

        driver.find_element(By.ID, "submit-button").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p[contains(text(),'Your request has been submitted successfully')]")
            )
        )

        return f"✅ CP_RF001_001 exitoso. Redirigido a: {driver.current_url}"

    except TimeoutException:
        return "❌ El mensaje de éxito no apareció. Puede que el registro falló o el CAPTCHA no fue validado correctamente."
    except NoSuchElementException as e:
        return f"❌ Campo del formulario no encontrado: {str(e)}"