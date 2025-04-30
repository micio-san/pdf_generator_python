import requests
from reportlab.pdfgen import canvas
from dotenv import load_dotenv
import os
body = {
"allergeni": "1",
"bromatologico": "1",
"dieId": "31",
"etaId": "42",
"piaId": "281",
"prodotti": "1"
}
load_dotenv()
api_url = os.getenv("API_URL")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

def draw(c, data):
    c.drawString(20,100,data["code"])
    c.setFont("Helvetica", 30)
    c.setFillColorRGB(100, 3, 67)
    c.drawString(20,20, data["desc"])
    c.setFont("Helvetica", 300)
    c.setFillColorRGB(100, 3, 67)
    c.showPage()
    c.save()
    
try:
    myReq = requests.post(api_url, headers=headers, json=body)
    myReq.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
    data=myReq.json()
except requests.exceptions.RequestException as e:
    print(f"error {e}")
else:
    c= canvas.Canvas("output.pdf")
    draw(c, data)
