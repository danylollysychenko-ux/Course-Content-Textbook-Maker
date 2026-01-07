import base64
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from sigmaboy import target_url

url = target_url
OUTPUT_PDF = "ecosystem.pdf"



def save_page_as_pdf(driver, url, output_file_name):
        # Force normal desktop rendering — NO scaling
    driver.execute_cdp_cmd(
        "Emulation.setDeviceMetricsOverride",
        {
            "width": 1920,
            "height": 1080,
            "deviceScaleFactor": 1,   # <- THIS is 100% zoom
            "mobile": False
        }
    )

    driver.get(url)

    # Allow JS, fonts, images, CSS to fully load
    time.sleep(5)

    # Print exactly what Chrome renders, with backgrounds
    pdf = driver.execute_cdp_cmd(
        "Page.printToPDF",
        {
            "printBackground": True,
            "preferCSSPageSize": True,
            "scale": 1,              # <- DO NOT SCALE
            "marginTop": 0.4,
            "marginBottom": 0.4,
            "marginLeft": 0.4,
            "marginRight": 0.4
        }
    )

    with open(OUTPUT_PDF, "wb") as f:
        f.write(base64.b64decode(pdf["data"]))

    print(f"Saved PDF at true 100% zoom: {OUTPUT_PDF}")



driver = webdriver.Chrome()

try:
    save_page_as_pdf(driver, url, OUTPUT_PDF)

finally:
    driver.quit()


 