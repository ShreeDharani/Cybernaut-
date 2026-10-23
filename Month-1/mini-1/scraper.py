import time
import pandas as pd
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

driver = uc.Chrome()

driver.get("https://coinmarketcap.com/")
time.sleep(5)

rows = WebDriverWait(driver, 30).until(
    EC.presence_of_all_elements_located((By.XPATH, '//table//tbody/tr'))
)

coins = []
for row in rows[:10]:
    try:
        name_cell = row.find_element(By.XPATH, './/td[3]')
        name = name_cell.text.split("\n")[0]

        price = row.find_element(By.XPATH, './/td[4]').text
        change_24h = row.find_element(By.XPATH, './/td[5]').text
        market_cap = row.find_element(By.XPATH, './/td[7]').text

        coins.append([name, price, change_24h, market_cap])
    except Exception as e:
        print("⚠️ Skipped a row due to error:", e)

df = pd.DataFrame(coins, columns=["Name", "Price", "24h Change", "Market Cap"])
df["Timestamp"] = pd.Timestamp.now()

file_name = "crypto_data.csv"
df.to_csv(file_name, mode="a", index=False, header=not os.path.exists(file_name))

print("✅ Correct data scraped and saved to crypto_data.csv")

driver.quit()
