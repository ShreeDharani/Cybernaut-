from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def scrape_reviews(product_url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.set_page_load_timeout(20)
    driver.get(product_url)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    reviews = []

    for r in soup.find_all("div", class_="text show-more__control"):
        text = r.get_text(strip=True)
        if text:
            reviews.append(text)

    if not reviews:
        reviews.append("No reviews found — site may be blocking Selenium.")

    return reviews
