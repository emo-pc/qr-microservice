# 🚀 Secure QR Code Microservice

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)

A lightweight, high-performance, and serverless microservice built with FastAPI that generates QR codes on the fly. Designed for modern cloud deployment architectures and secured with API key validation.

## ✨ Features
- **Fast & Asynchronous:** Built on top of FastAPI and Uvicorn for maximum performance.
- **Secure Endpoint:** Protected via query parameter API key validation (401 Unauthorized for invalid requests).
- **Containerized:** Includes a fully configured, production-ready Dockerfile (using python:3.10-slim).
- **Cloud-Ready:** Dynamic port binding configured for seamless continuous deployment on platforms like Render.
- **Client Integration:** Includes a sample Python client (client.py) for immediate use in other applications.

---

## 📂 Project Structure
- `main.py` - Main FastAPI application and routing
- `test.py` - Sample Python script to consume the API
- `Dockerfile` - Docker configuration for deployment
- `requirements.txt` - Python dependencies
- `.gitignore` - Ignored files

---

## 🛠️ Getting Started (Local Development)

   Option : Using Docker 🐳
1. Build the Docker image:
   `docker build -t qr-microservice .`
2. Run the container:
   `docker run -p 8080:10000 qr-microservice`

---

## ☁️ Live API Usage

The API is deployed and exposes a secure `/generate` endpoint. It returns a `image/png` response containing the QR Code.

### Request Format
**Endpoint:** `GET /generate`
- `api_key` (string, Required): Your secret password for authentication.
- `text` (string, Required): The data/URL you want to encode into the QR code.

**Example URL Request:**
`https://YOUR-APP-NAME.onrender.com/generate?api_key=magna_carta_libertatum&text=Hello+Cloud`

---

## 🐍 Using the Client (`test.py`)

You can easily consume this API from any backend service or automation script. Just run the included client script:
`python test.py`

