from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.common import abrir_formulario_registro

def esperar_y_verificar_error(driver, aria_label, mensaje_esperado):
    try:
        error_div = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located(
                (By.XPATH, f"//div[@role='alert' and @aria-describedby='{aria_label}']")
            )
        )
        assert mensaje_esperado in error_div.text.strip()
        print(f"✅ Error mostrado correctamente para '{aria_label}': {mensaje_esperado}")
        return True
    except Exception as e:
        print(f"❌ No se mostró el mensaje de error esperado para '{aria_label}': {str(e)}")
        return False

def run(driver):
    if not abrir_formulario_registro(driver):
        return "❌ Error al abrir el formulario."

    resultados = []

    try:
        campos = {
            "name": "Valentina Chambi",
            "institution": "Universidad Nacional de Colombia",
            "country": "Colombia",
            "email": "vchambilla@universidad.edu.co"
        }

        errores = {
            "name": "Please enter your name.",
            "institution": "Please enter your institution name.",
            "country": "Please enter your institution's country.",
            "email": "Please enter your email address."
        }

        for campo_vacio in campos.keys():
            # Limpiar todos los campos
            for id_, valor in campos.items():
                input_field = driver.find_element(By.ID, id_)
                input_field.clear()
                if id_ != campo_vacio:
                    input_field.send_keys(valor)

            # Clic en el botón de submit usando JavaScript
            submit_btn = driver.find_element(By.ID, "submit-button")
            driver.execute_script("arguments[0].click();", submit_btn)
            print(f"🧪 Validando error cuando falta el campo: {campo_vacio}")

            # Esperar el mensaje de error esperado
            ok = esperar_y_verificar_error(driver, f"{campo_vacio}-label", errores[campo_vacio])
            resultados.append((campo_vacio, ok))

    except Exception as e:
        return f"❌ Error durante la ejecución del caso CP_RF001_002: {str(e)}"

    # Resumen final
    if all(r[1] for r in resultados):
        return "✅ CP_RF001_002 exitoso: todos los errores se mostraron correctamente."
    else:
        errores = ', '.join([r[0] for r in resultados if not r[1]])
        return f"⚠️ CP_RF001_002 parcialmente exitoso. Fallaron: {errores}"

