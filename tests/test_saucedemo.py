import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from selenium.webdriver.common.by import By
from utils.helpers import iniciar_navegador, cerrar_navegador

@pytest.fixture
def setup():
    driver = iniciar_navegador()
    yield driver
    cerrar_navegador(driver)

def test_login_exitoso(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")

    # Ingreso de credenciales
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Validar login correcto
    assert "inventory.html" in driver.current_url, "No se redirigió al inventario"
    assert "Products" in driver.page_source, "No se encontró el texto 'Products'"

    import pytest
from selenium.webdriver.common.by import By
from utils.helpers import iniciar_navegador, cerrar_navegador

@pytest.fixture
def setup():
    driver = iniciar_navegador()
    yield driver
    cerrar_navegador(driver)


# ---------- TEST 1: LOGIN EXITOSO ----------
def test_login_exitoso(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory.html" in driver.current_url, "No se redirigió al inventario"
    assert "Products" in driver.page_source, "No se encontró el texto 'Products'"


# ---------- TEST 2: CATÁLOGO / INVENTARIO ----------
def test_catalogo_inventario(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")

    # Login antes de validar inventario
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Validar título
    titulo = driver.find_element(By.CLASS_NAME, "title").text
    assert titulo == "Products", f"Título incorrecto: {titulo}"

    # Verificar que haya productos visibles
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No hay productos visibles"

    # Validar que existan elementos importantes (menú, filtro)
    assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed(), "No se encontró el menú"
    assert driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed(), "No se encontró el filtro"

    # Mostrar nombre y precio del primer producto
    primer_producto_nombre = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    primer_producto_precio = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"\nPrimer producto: {primer_producto_nombre} - Precio: {primer_producto_precio}")

    # ---------- TEST 3: CARRITO ----------
def test_agregar_producto_al_carrito(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Agregar primer producto al carrito
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()

    # Validar contador del carrito
    contador = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert contador == "1", f"El contador del carrito no se actualizó: {contador}"

    # Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Validar que el producto esté en el carrito
    producto_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert producto_en_carrito != "", "No se encontró el producto en el carrito"
    print(f"\nProducto agregado al carrito: {producto_en_carrito}")