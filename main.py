from utils.driver import get_driver
from modules import CP_RF001_001, CP_RF001_002, CP_RF001_003, CP_RF021_001, CP_RF021_003, CP_RF021_002
from utils.common import login_como_instructor

def main():
    driver = get_driver()

    try:
        print("🔹 Ejecutando caso RF-001: Registro de Instructor")
        # result = CP_RF001_001.run(driver)
        # print(result)

        # LOGIN INSTRUCTOR
        print("🔹 Iniciando login como instructor para probar RF-0021")
        if not login_como_instructor(driver):
            return print("⚠️ No se pudo autenticar. Revisa manualmente.")

        print("🔹 Ejecutando caso RF-0021: --")
        print("CP_RF021_001:")
        result = CP_RF021_001.run(driver)
        print(result)
        print("CP_RF021_002:")
        result = CP_RF021_002.run(driver)
        print(result)
        print("CP_RF021_003:")
        result = CP_RF021_003.run(driver)
        print(result)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
