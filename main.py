from utils.driver import get_driver
from modules import RF_001  # Importar con guión bajo por convención de Python

def main():
    driver = get_driver()

    try:
        print("🔹 Ejecutando caso RF-001: Registro de Instructor")
        result = RF_001.run(driver)
        print(result)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
