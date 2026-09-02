import requests

# Render'ın sana verdiği URL'yi buraya yapıştır
BASE_URL = "https://qr-microservice-3a0r.onrender.com"

# API'ye göndereceğimiz parametreler (Şifremiz ve QR'a çevrilecek metin)
parametreler = {
    "api_key": "magna_carta_libertatum?",
    "text": "Selam Cloud dünyası! Bu QR kod Render sunucularından geldi."
}

print("Buluttaki API'ye istek atılıyor...")
response = requests.get(BASE_URL, params=parametreler)

# Gelen cevabı kontrol et
if response.status_code == 200:
    # 200 OK ise gelen bayt (byte) verisini PNG olarak kaydet
    with open("buluttan_gelen_qr.png", "wb") as dosya:
        dosya.write(response.content)
    print("✅ Başarılı! QR Kod 'buluttan_gelen_qr.png' adıyla kaydedildi.")
else:
    print(f"❌ Hata oluştu: {response.status_code}")
    print(response.text)