from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def iniciar_navegador():
    """Inicia el navegador Chrome y lo devuelve."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service()  # Usa el ChromeDriver instalado en tu PATH
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)
    return driver

def cerrar_navegador(driver):
    """Cierra el navegador."""
    time.sleep(5)
    driver.quit()