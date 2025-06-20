from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.common import login_como_instructor
import time

def run(driver):
    try:
        driver.get("https://arania-teammates.appspot.com/web/instructor/courses")
        print("🔄 Redirigido directamente al formulario de creación de curso.")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "active-courses-table"))
        )

        print("🔍 Tabla de cursos encontrada.")

        primer_tr = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#active-courses-table tbody tr"))
        )

        course_id = primer_tr.find_element(By.ID, "course-id-0").text.strip()
        course_name = primer_tr.find_elements(By.TAG_NAME, "td")[1].text.strip()

        print(f"📘 Primer curso en tabla: ID = {course_id}, Nombre = {course_name}")

        btn_acciones = primer_tr.find_element(By.ID, "btn-other-actions-0")
        btn_acciones.click()
        time.sleep(0.5)

        # Hacer clic en "Delete"
        btn_eliminar = primer_tr.find_element(By.ID, "btn-soft-delete-0")
        btn_eliminar.click()
        print("🗑️ Botón 'Delete' presionado.")

        # Esperar a que aparezca el modal de confirmación
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "modal-footer"))
        )

        # Hacer clic en "Yes"
        botones_modal = driver.find_elements(By.CSS_SELECTOR, ".modal-footer button")
        for boton in botones_modal:
            if boton.text.strip().lower() == "yes":
                boton.click()
                break

        print("✅ Confirmación de eliminación enviada.")

        # Esperar el toast de confirmación de eliminación
        toast = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "toast-body"))
        )

        mensaje = toast.text.strip()
        if "has been deleted" in mensaje.lower():
            print(f"🟢 {mensaje}")
            return "✅ Curso eliminado correctamente."
        else:
            return f"⚠️ Toast inesperado: {mensaje}"

    except TimeoutException:
        return "❌ CP-RF021-003 fallido: No apareció mensaje de error tras intentar crear un curso duplicado."
    except Exception as e:
        return f"❌ Error inesperado: {str(e)}"
