import os.path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService



def create_driver(url="http://shell.personal-order.cs.house", firefox=False, screen_size=(1400, 1400)):
    if firefox:
        options = webdriver.FirefoxOptions()
    else:
        options = webdriver.ChromeOptions()

    options.add_argument("--window-size=%s,%s" % screen_size)
    if firefox:
        return webdriver.Remote(
            command_executor=url,
            options=options
        )
    else:
        return webdriver.Remote(
            command_executor=url,
            options=options
        )


def create_local_driver(firefox=False, headless=False, screen_size=(3000, 3000)):
    if firefox:
        service = FirefoxService()
        options = webdriver.FirefoxOptions()
    else:
        service = ChromeService()
        options = webdriver.ChromeOptions()

    if headless:
        options.add_argument("--headless")
    options.add_argument("--window-size=3000, 3000")
    if firefox:
        print("Downloaded Firefox driver. Starting Firefox.")
        return webdriver.Firefox(service=service, options=options)
    else:
        try:
            return webdriver.Chrome(service=service, options=options)
        except Exception as e:
            print(e)
            print("Unable to use Chrome. Using Firefox instead.")
            return webdriver.Firefox(service=service, options=options)

if __name__ == "__main__":
    driver = create_local_driver(headless=True)
    driver.get("https://www.youtube.com")
    driver.save_screenshot(os.path.join(os.getcwd(), "test.png"))

