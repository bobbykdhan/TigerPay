import time

from webdriver_handler import *
from login import *
from image import *
import requests

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def get_card(verbose=True):
    load_dotenv()
    driver = create_local_driver(headless=True)

    if verbose: print("Created Driver")

    wait = WebDriverWait(driver, 50, poll_frequency=1)
    driver.get("http://tigerspend.rit.edu")
    if verbose: print("Started sign in")
    sign_in(driver, url="https://tigerspend.rit.edu/login.php?cid=105&wason=/virtualcardnew.php")
    try:
        wait.until(ec.visibility_of_element_located((By.ID, "frontimage")))
    except Exception as e:
        send_text(f"An error occurred while logging in (probably an out of sync DUO count - {os.getenv('COUNT')})")
        return

    if verbose: print("Successfully logged in")

    card_link = driver.find_element(By.ID, "frontimage").get_attribute("src")
    save_path = os.path.abspath("./screenshots/screen.png")

    response = requests.get(card_link)
    with (open(save_path, 'wb') as file):

        if response.status_code == 200:
            file.write(response.content)
            if verbose: print("Saved image")
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
            send_text("An error occurred while downloading image")
            return

    print("Card image is at " + upload_screenshot(driver,send_text=True, new_pic=False, filename="screen"))

    driver.quit()



if __name__ == "__main__":
    get_card()