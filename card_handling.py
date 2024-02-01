import time

from webdriver_handler import *
from login import *
from image import *
import requests

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def get_card():
    load_dotenv()
    driver = create_local_driver(headless=False)
    wait = WebDriverWait(driver, 50, poll_frequency=1)
    driver.get("http://tigerspend.rit.edu")
    sign_in(driver, url="https://tigerspend.rit.edu/login.php?cid=105&")

    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "jsa_main-nav")))
    driver.get("https://tigerspend.rit.edu/virtualcardnew.php?")


    wait.until(ec.visibility_of_element_located((By.ID, "frontimage")))

    card_link = driver.find_element(By.ID, "frontimage").get_attribute("src")

    save_path = os.path.abspath("./screenshots/screen.png")

    response = requests.get(card_link)
    with open(save_path, 'wb') as file:
        file.write(response.content) if response.status_code == 200 else print(
            f"Failed to download image. Status code: {response.status_code}")

    print("Card image is at " + upload_screenshot(driver,send_text=True, new_pic=False, filename="screen"))

    return driver



if __name__ == "__main__":
    get_card()