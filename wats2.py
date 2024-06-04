from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def enviar_imagen_whatsapp(numero, ruta_imagen):
    # Inicializar el navegador
    driver = webdriver.Chrome()

    try:
        # Abrir WhatsApp Web
        driver.get("https://web.whatsapp.com/")

        # Esperar hasta que el usuario escanee el código QR manualmente
        WebDriverWait(driver, 30).until(EC.title_contains("WhatsApp"))

        # Buscar el chat del destinatario
        input_chat = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))
        input_chat.send_keys(numero)
        input_chat.send_keys(Keys.ENTER)

        # Adjuntar la imagen
        adjuntar_icono = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@title="Adjuntar"]')))
        adjuntar_icono.click()

        # Seleccionar la opción "Fotos"
        adjuntar_imagen = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')))
        adjuntar_imagen.send_keys(ruta_imagen)

        # Esperar a que se cargue la imagen antes de enviar
        time.sleep(2)

        # Enviar la imagen
        enviar_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]')))
        enviar_btn.click()

        # Esperar un momento antes de cerrar el navegador
        time.sleep(100)

    except Exception as e:
        print("Ocurrió un error:", e)

    finally:
        driver.quit()

# Ejemplo de uso
if __name__ == "__main__":
    numero = "52 1 712 224 5749"  
    ruta_imagen = r"C:\Users\Admi\Documents\Python\Lenovo3.jpg"  

    enviar_imagen_whatsapp(numero, ruta_imagen)
