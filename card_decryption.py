from fastapi import FastAPI
from pylibdmtx.pylibdmtx import decode
from PIL import Image
from bs4 import BeautifulSoup as bs4
import requests

app = FastAPI()





@app.get("/card")
async def read_item(skey: str = 0, cid: str = "105", side: str = ""):

    payload = {
        'skey': skey,
        'cid': cid,
        'side': "front"
    }
    # Change this to use selenium to at least get the cookies and try to use reuwsts with it
    card = requests.get(
        "https://tigerspend.rit.edu/" + 'imagestudentcard.php?cid=105&skey=' + payload["skey"] + '&side=front')





    with open('card.jpg', 'wb') as handler:
        handler.write(card.content)
        im = Image.open(r"card.jpg")

        im1 = im.crop((250, 685, 451, 885))
        im1.show()
        im1.save("crop.png")
        code = decode(Image.open("crop.png"))[0].data

        im.show()
        print(code)
        return {"The Code":code }

