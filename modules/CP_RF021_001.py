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

        driver.find_element(By.ID, "course-id").send_keys("ALG2025S3")
        driver.find_element(By.ID, "course-name").send_keys("Evaluación Álgebra Prueba 01")

        # Los selects tienen una opción por defecto ya visible, no se cambian
        submit_btn = driver.find_element(By.ID, "btn-submit-course")
        if not submit_btn.is_enabled():
            return "❌ CP-RF021-001: El botón de 'Add Course' está deshabilitado pese a campos válidos."

        submit_btn.click()
        time.sleep(5)

        toast = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "toast-body"))
        )
        toast_text = toast.text.strip()

        if toast_text == "The course has been added.":
            return "✅ CP-RF021-001 exitoso: Curso creado correctamente."
        else:
            return f"❌ CP-RF021-001 fallido: Toast inesperado: {toast_text}"

    except TimeoutException:
        return "❌ No se encontró el formulario de curso tras redirección directa."
    except Exception as e:
        return f"❌ Error inesperado en CP-RF021-001: {str(e)}"
