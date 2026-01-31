from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def scrape_website(url: str = "https://jorgebenitezlopez.com") -> list[dict]:
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)

        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h1"))
        )

        scraped_data = []

        # Ejemplo simple: solo h1 (datos coherentes)
        titles = driver.find_elements(By.CSS_SELECTOR, "h1")

        for title in titles:
            scraped_data.append({
                "title": title.text,
                "url": url,
            })

        return scraped_data

    except Exception as e:
        # En Django: logging.exception(e)
        print("Error durante el scraping:", e)
        return []

    finally:
        # ✔️ SIEMPRE se ejecuta
        driver.quit()
