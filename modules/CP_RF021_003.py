from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.common import login_como_instructor
import time

def run(driver):
    try:
        driver.get("https://arania-teammates.appspot.com/web/instructor/courses?isAddNewCourse=true")
        print("🔄 Redirigido directamente al formulario de creación de curso.")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "add-course-section"))
        )

        print("✅ Formulario de curso visible.")

        driver.find_element(By.ID, "course-id").send_keys("ALG2025S3")  # ID duplicado
        driver.find_element(By.ID, "course-name").send_keys("Química Básica Prueba 01")
        driver.find_element(By.ID, "course-institute").click()  # Ya hay opción por defecto
        driver.find_element(By.ID, "btn-submit-course").click()

        time.sleep(5)

        toast = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "toast-body"))
        )
        toast_text = toast.text.strip()

        if "has been used by another course" in toast_text:
            return "✅ CP-RF021-003 exitoso: Se detectó mensaje de error por ID duplicado."
        else:
            return f"❌ CP-RF021-003 fallido: El toast apareció, pero con mensaje inesperado: {toast_text}"

    except TimeoutException:
        return "❌ CP-RF021-003 fallido: No apareció mensaje de error tras intentar crear un curso duplicado."
