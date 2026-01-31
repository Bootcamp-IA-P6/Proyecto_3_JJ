from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Para Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def scrape_website():
    # Configurar Selenium
    options = Options()

    # OK: headless es correcto para scraping
    options.add_argument('--headless')

    # OK en servidores Linux / contenedores
    # En Windows no es estrictamente necesario, pero no molesta
    options.add_argument('--no-sandbox')

    # OK: evita errores de memoria en entornos limitados
    options.add_argument('--disable-dev-shm-usage')

    # ⚠️ webdriver-manager se ejecuta CADA VEZ que llamas a la función
    # Funciona, pero es costoso.
    # Más adelante convendría inicializarlo una sola vez.
    service = Service(ChromeDriverManager().install())

    # Inicialización correcta del driver
    driver = webdriver.Chrome(service=service, options=options)

    # URL hardcodeada → aceptable para el ejercicio,
    # pero mejor recibirla como parámetro
    url = "https://jorgebenitezlopez.com"
    driver.get(url)

    # ✔️ Útil para depuración, ❌ no ideal en producción
    print(driver.title)

    # ❌ Problema de estilo:
    # Este comentario debería estar indentado como el código
    # (no rompe nada, pero es confuso)
    # Esperar a que los elementos estén presentes
    try:
        # ✔️ Bien: WebDriverWait en lugar de time.sleep
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h1"))
        )

        # ⚠️ Aquí hay un problema lógico:
        # Estás obteniendo TODOS los <h1> y TODOS los <a>
        # y luego los unes con zip().
        # No hay garantía de que correspondan entre sí.
        titles = driver.find_elements(By.CSS_SELECTOR, "h1")
        urls = driver.find_elements(By.CSS_SELECTOR, "a")

    except Exception as e:
        # ❌ print en lugar de logging
        print("Error al encontrar los elementos:", e)

        # ❌ driver.quit() aquí...
        driver.quit()
        return []

    scraped_data = []

    # ⚠️ zip(titles, urls) puede:
    # - perder elementos
    # - mezclar datos incorrectos
    for title, link in zip(titles, urls):
        scraped_data.append({
            "title": title.text,
            "url": link.get_attribute("href"),
        })

    # ✔️ útil para depuración
    print("Scraped data:", scraped_data)

    # ❌ driver.quit() solo se ejecuta si NO hubo excepción
    # Si algo falla antes, el navegador puede quedar abierto
    driver.quit()

    return scraped_data
