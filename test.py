from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. Initialize the WebDriver (e.g., Chrome)
# Ensure the path to your chromedriver executable is correct
driver = webdriver.Chrome()

try:
    # 2. Navigate to a website
    driver.get("https://ects-cmp.com/course_content/python-bro-code-style/" \
    "")
    #driver.get("https://ects-cmp.com/course_content/wp-login.php?redirect_to=https%3A%2F%2Fects-cmp.com%2Fcourse_content%2F")
    print(f"Page title: {driver.title}")

    # Example using By.ID
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".wpo365-mssignin-button"))
    )
    element.click()


    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=email]"))
    )
    element.send_keys("cmp_dalysychenko@ects.org")

    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#idSIButton9"))
    )
    element.click()


    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=password]"))
    )
    element.send_keys("Ects0719")

    input()
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#idSIButton9"))
    )
    element.click()


    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#idBtn_Back"))
    )
    element.click()
    wait = WebDriverWait(driver, 10)
    elements = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".menu-item")))
    # wait = WebDriverWait(driver, 5)
    menu_items = driver.find_elements(By.CSS_SELECTOR, ".menu-item")
    sub_menu_items = driver.find_elements(By.CSS_SELECTOR, ".sub-menu .menu-item")
    # for item in menu_items:
    #     print(item.text)
    
    for item in sub_menu_items:
        print(item.text)

    links = driver.find_elements(By.CSS_SELECTOR, ".sub-menu .menu-item a")
    hrefs = [l.get_attribute("href") for l in links if l.get_attribute("href")]

    for url in hrefs:
        driver.get(url)
        print(f"Visited: {url}")
        time.sleep(1)
    hold = input("Press enter to close ")

finally:
    # 7. Close the browser
    driver.quit()
    print("Browser closed.")