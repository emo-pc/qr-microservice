import requests

#you have to write down your own url below
BASE_URL = "https://qr-microservice-3a0r.onrender.com/generate"

parametreler = {
    #you can change the password
    "api_key": "magna_carta_libertatum",
    "text": "Boğaziçi CmpE Cloud Test"
}

response = requests.get(BASE_URL, params=parametreler)

print(f"Server answer: {response.status_code}")

if response.status_code == 200:
    with open("qr.png", "wb") as f:
        f.write(response.content)
    print("✅ success.")
else:
    print(f"❌ error: {response.text}")