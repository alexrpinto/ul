from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime, timedelta
import time

# Punto 1: Definir las variables de usuario y contraseña
User = "A601051290049"
Password_file = "C:/Users/josealejandro.rodrig/Desktop/python/password.txt"
Website = "https://www.canalpremium.telefonica.es/"
path = "C:/Users/josealejandro.rodrig/Desktop/python/chromedriver.exe"

# Punto 2: Leer la contraseña desde el archivo de texto
with open(Password_file, 'r') as file:
    Password = file.read().replace('\n', '')

# Punto 3: Iniciar el navegador y abrir la página web
service = webdriver.chrome.service.Service(path)
driver = webdriver.Chrome(service=service)
driver.get(Website)
time.sleep(5)

# Punto 4: Ingresar el nombre de usuario
input_user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#usr_name')))
input_user.send_keys(User)

# Punto 5: Ingresar la contraseña
input_pass = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#pgeac')))
input_pass.send_keys(Password)

# Punto 7: Hacer clic en el botón de inicio de sesión
submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#botonEntrar button')))
submit_button.click()
time.sleep(10)

# punto 8: hacer click en el botón de inicio de sesión numero 2
submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.gtm_clic_enlace_Servicios-Grabador.en.red')))
submit_button.click()
time.sleep(80)

# cambiar de manejador de ventana activo
driver.switch_to.window(driver.window_handles[1])

# Obtener el manejador de ventana activo
current_window_handle = driver.current_window_handle

# Obtener el título de la página actual
current_title = driver.title

# Comprobar si el título de la página actual es el que se espera
if current_title == "Grabador en Red":
    print("Se ha cambiado a la segunda pestaña correctamente")
else:
    print("No se ha cambiado a la segunda pestaña")

def fill_date_range(driver):
    # localizar botones de fechas de inicio y final
    start_date_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#StartDate')))
    end_date_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#EndDate')))

    # calcular el rango de fecha que se desea segun el dia de la semana
    current_day = datetime.now()
    previous_day = current_day - timedelta(days=1)
    if current_day.weekday() == 0:  # esto es el dia lunes
        time_span_length = 2
    else:
        time_span_length = 1
    previous_day -= timedelta(days=time_span_length)

    # Formatos de fecha en forma de strings
    start_date_string = previous_day.strftime("%Y-%m-%d") + " 00:00"
    end_date_string = current_day.strftime("%Y-%m-%d") + " 23:55"

    # rellenar los campos de fecha
    start_date_input.clear()
    start_date_input.send_keys(start_date_string)
    end_date_input.clear()
    end_date_input.send_keys(end_date_string)

search_button = WebDriverWait(driver, 15).until(lambda driver: driver.find_element(By.CSS_SELECTOR, "button#searchSubmit.btn.btn-sm.green.btn-outline.filter-submit.margin-bottom"))
search_button.click()

time.sleep(10)

wait = WebDriverWait(driver, 10)

# generar archivo
search_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.CSS_SELECTOR, 'div.actions div.btn-group a.btn.styledlist'))
search_button.click()



search_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.CSS_SELECTOR, 'ul.dropdown-menu li:nth-child(1) a'))
search_button.click()



# Esperar hasta que la descarga esté completa

search_button = wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
