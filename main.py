import requests
from reportlab.pdfgen import canvas

api_url = ""
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
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
