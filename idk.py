import time


from image import upload_screenshot
from webdriver_handler import *
from order_manager import *


def debug_screenshot():
    driver = create_driver(firefox=True)
    dotenv.load_dotenv()
    driver.get("https://www.youtube.com")
    print("Created driver")
    time.sleep(10)
    upload_screenshot(driver, True, True)
    print("Uploaded screenshot")



def debug(driver=None):
    if driver is None:
        driver = create_local_driver()
    wait = WebDriverWait(driver, 150, poll_frequency=1)
    # Opens the ondemand website
    driver.get("https://ondemand.rit.edu/")
    selectStore(driver, "Sol's")
    items = selectCategory(driver, "Beverages")
    selectedItems = []
    selectedItems.append(select_item(items, "Aquafina Water 20 oz"))
    selectedItems.append(select_item(items, "Schweppes Ginger Ale"))

    for item in selectedItems:
        addToCart(driver, items, item, {}, "Look how cool I am")

    items = selectCategory(driver, "Ice Cream")
    selectedItems = []
    addToCart(driver, items, select_item(items, "Shake"), {"Shake Choices":"Strawberry"}, "Look how cool I am")

    other_open_login(driver)
    sign_in(driver)
    wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "cart-icon")))
    driver.find_element(By.CLASS_NAME, "cart-icon").click()



    return driver, items



def debug2(driver=None):

    if driver is None:
        driver = create_local_driver()
    wait = WebDriverWait(driver, 150, poll_frequency=1)
    # Opens the ondemand website
    items = commons_burger(driver)

    # fulfillment("bobby","d", os.getenv("PHONE_NUMBER"), driver)
    return driver, items

def breakfast(driver,amount=2, add_drink=True):
    driver.get("https://ondemand.rit.edu/")
    selectStore(driver, "Ctrl Alt DELi")
    items = selectCategory(driver, "Breakfast")
    selectedItem = select_item(items, "Bagel, Egg, and Cheese Sandwich")
    for i in range(amount):
        addToCart(driver, items, selectedItem, {"Cheese": "Extra Cheese"}, "On a roll please")
    if add_drink:
        items = selectCategory(driver, "Beverages")
        selectedItem = select_item(items, "Tropicana Apple Juice")
        addToCart(driver, items, selectedItem)
    return items
def commons_burger(driver, amount=1):

    driver.get("https://ondemand.rit.edu/")
    selectStore(driver, "The Commons")
    items = selectCategory(driver, "Grill")
    selectedItem = select_item(items, "Black Bean Burger")
    for i in range(amount):
        addToCart(driver, items, selectedItem, {"Add Cheese?": "American Cheese"})
    return items


def idk():
    modifierChoices = [{"Group": "Item"}, {"Group": "Item"}]


