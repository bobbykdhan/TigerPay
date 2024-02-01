import time

from webdriver_handler import *
from login import *
from image import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def get_card():
    load_dotenv()
    driver = create_local_driver(headless=True)
    wait = WebDriverWait(driver, 50, poll_frequency=1)
    driver.get("http://tigerspend.rit.edu")
    sign_in(driver, url="https://tigerspend.rit.edu/login.php?cid=105&")
    while "https://tigerspend.rit.edu/" not in driver.current_url:
        time.sleep(0.1)
    driver.get("https://tigerspend.rit.edu/virtualcardnew.php?")


    wait.until(ec.visibility_of_element_located((By.ID, "frontimage")))

    card_link = driver.find_element(By.ID, "frontimage").get_attribute("src")

    driver.get(card_link)
    time.sleep(1)
    print("Card image is at" + upload_screenshot(driver,send_text=True))

    return driver



if __name__ == "__main__":
    get_card()