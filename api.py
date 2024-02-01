import asyncio
import time

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, BackgroundTasks, Response, Form
from twilio.twiml.messaging_response import MessagingResponse

import card_handling
from image import upload_screenshot

from webdriver_handler import *

load_dotenv()

app = FastAPI()


global driver



@app.get("/")
async def root():
    return {"message": "Hello World"}


async def getcard():
    await asyncio.to_thread(card_handling.get_card)

@app.get("/get_card")
async def get_card(BackgroundTasks: BackgroundTasks):
    BackgroundTasks.add_task(getcard)
    return {"message": "Card requested"}



@app.get('/sms')
@app.post('/sms')
async def chat(From: str = Form(...), Body: str = Form(...)):
    response = MessagingResponse()
    response.message(f"Placeholder")
    print(f"Text from: {From} and contains: {Body}")
    return Response(content=str(response), media_type="application/xml")
    # return {"message": f"Text from: {From} and contains: {Body}"}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

#TODO make this work
