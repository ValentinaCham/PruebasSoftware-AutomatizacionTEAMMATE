from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.common import abrir_formulario_registro
from selenium.webdriver.common.keys import Keys

def run(driver):
    if not abrir_formulario_registro(driver):
        return "❌ Error al abrir el formulario."

    try:

        driver.find_element(By.ID, "name").send_keys("Valentina Chambi")
        driver.find_element(By.ID, "institution").send_keys("Universidad Nacional de Colombia")
        driver.find_element(By.ID, "country").send_keys("Colombia")
        driver.find_element(By.ID, "email").send_keys("vchambilla@universidad.edu.co")
        driver.find_element(By.ID, "comments").send_keys("")

        try:
            # Cambiar al iframe que contiene el recaptcha
            WebDriverWait(driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='reCAPTCHA']"))
            )

            # Clic en el checkbox del recaptcha
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "recaptcha-checkbox-border"))
            ).click()

            print("🔘 reCAPTCHA clickeado.")

            driver.switch_to.default_content()

            print("🔄 Volviendo al formulario principal.")

            driver.find_element(By.ID, "name").send_keys("Verificacion")
            # driver.find_element(By.ID, "submit-button").click()
            driver.execute_script("""
                document.getElementById('name').dispatchEvent(new Event('input'));
                document.getElementById('submit-button').click();
            """)
            print("✅ Formulario enviado, esperando mensaje de éxito...")

            # email_field = driver.find_element(By.ID, "email")
            # email_field.send_keys(Keys.ENTER)
            # print("⏎ ENTER enviado al campo email.")

            WebDriverWait(driver, 50).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//p[normalize-space(text())='Your request has been submitted successfully:']")
                )
            )


            return f"✅ CP_RF001_001 exitoso. Redirigido a: {driver.current_url}"
    
        except Exception as e:
            return f"⚠️ No se pudo interactuar con el reCAPTCHA: {str(e)}"


    except TimeoutException:
        return "❌ El mensaje de éxito no apareció. Puede que el registro falló o el CAPTCHA no fue validado correctamente."
    except NoSuchElementException as e:
        return f"❌ Campo del formulario no encontrado: {str(e)}"