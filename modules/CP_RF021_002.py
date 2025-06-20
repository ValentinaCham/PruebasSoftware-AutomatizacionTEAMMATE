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
            EC.presence_of_element_located((By.ID, "add-course-section"))
        )

        exitosos = 0

        # Caso 1: Ambos vacíos
        driver.find_element(By.ID, "course-id").clear()
        driver.find_element(By.ID, "course-name").clear()
        time.sleep(2)
        submit_button = driver.find_element(By.ID, "btn-submit-course")
        estado1 = not submit_button.is_enabled()
        print(f"{'✅' if estado1 else '❌'} Ambos vacíos → Botón {'deshabilitado' if estado1 else 'habilitado'}")
        exitosos += 1 if estado1 else 0

        # Caso 2: Solo course-id vacío
        driver.find_element(By.ID, "course-name").send_keys("Curso de Prueba")
        driver.find_element(By.ID, "course-id").clear()
        time.sleep(2)
        estado2 = not submit_button.is_enabled()
        print(f"{'✅' if estado2 else '❌'} Course ID vacío → Botón {'deshabilitado' if estado2 else 'habilitado'}")
        exitosos += 1 if estado2 else 0

        # Caso 3: Solo course-name vacío
        driver.find_element(By.ID, "course-id").send_keys("ID12345")
        driver.find_element(By.ID, "course-name").clear()
        time.sleep(2)
        estado3 = not submit_button.is_enabled()
        print(f"{'✅' if estado3 else '❌'} Course Name vacío → Botón {'deshabilitado' if estado3 else 'habilitado'}")
        exitosos += 1 if estado3 else 0

        if exitosos == 3:
            return "✅ Prueba Completa"
        elif exitosos >= 1:
            return "⚠️ Falla Parcial"
        else:
            return "❌ Falla Total"

    except TimeoutException:
        return "❌ No se encontró el formulario de curso tras redirección directa."
    except Exception as e:
        return f"❌ Error inesperado en CP-RF021-001: {str(e)}"
