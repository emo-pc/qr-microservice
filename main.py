from fastapi import FastAPI,Depends,HTTPException,Query
from fastapi.responses import Response
import qrcode
import io


app=FastAPI(
    title="QR Code Microservice",
    description="API working on Render CLoud "
)
#you can change the password
password="magna_carta_libertatum"

def check_pass(api_key:str=Query(...,description="Enter the password")):
    if api_key!=password:
        raise HTTPException(status_code=401,detail="Wrong password")
@app.get("/")
def main_page():
    return {"message":"To create qr code, request /generate?text=your_text"}

@app.get("/generate",dependencies=[Depends(check_pass)])
def create_qr(text:str=Query(...,description="Enter the text")):
    img =qrcode.make(text)

    buf =io.BytesIO()
    img.save(buf,format="PNG")
    image_bytes=buf.getvalue()
    return Response(content=image_bytes,media_type="image/png")

