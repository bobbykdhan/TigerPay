import time

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, BackgroundTasks, Response, Form
from twilio.twiml.messaging_response import MessagingResponse

import main2
from image import upload_screenshot
from order_manager import *
from webdriver_handler import *

load_dotenv()

app = FastAPI()

# my_twilio.send_text("Personal Order server started")

global driver



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/get_card")
async def get_card(BackgroundTasks: BackgroundTasks):
    BackgroundTasks.add_task(main2.get_card() )
    return {"message": "Card requested"}





@app.get("/testScreenshot")
async def testScreenshot():
    driver = create_driver()
    driver.get("https://www.youtube.com")
    print("Created driver")
    time.sleep(5)
    link = upload_screenshot(driver, True, True)
    print("Uploaded screenshot")
    return {"message": "Screenshot is at: " + link}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

#TODO make this work
