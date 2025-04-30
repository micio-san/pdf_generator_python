import requests
from reportlab.pdfgen import canvas

api_url = "https://testh.ristonova.it/novasrvdiet/public/v1/1/piattocompleto/fasciaeta"
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
body = {
"allergeni": "1",
"bromatologico": "1",
"dieId": "31",
"etaId": "42",
"piaId": "281",
"prodotti": "1"
}

def draw(c, data):
    c.drawString(20,20,data["code"])
    c.showPage()
    c.save()
    c.setFont("Helvetica", 30)
    
try:
    myReq = requests.post(api_url, headers=headers, json=body)
    myReq.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
    data=myReq.json()
except requests.exceptions.RequestException as e:
    print(f"error {e}")
else:
    c= canvas.Canvas("output.pdf")
    draw(c, data)