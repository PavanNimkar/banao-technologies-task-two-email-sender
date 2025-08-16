# 📧 Django Email API (Serverless + Offline + DRF)

This project is a simple **Django REST Framework (DRF) API** built with the **Serverless Framework**.  
It allows you to send emails using **Gmail SMTP** via a REST API.

⚡ Currently, the project runs **locally using `serverless-offline`**.  
AWS deployment is **not included** in this repo.

---

## 🚀 Features
- Django REST Framework (DRF) API for sending emails
- Function-Based View (FBV) for handling requests
- Configured with Gmail SMTP
- Uses **Serverless Framework** with `serverless-wsgi`
- Runs **offline locally** (no AWS deployment yet)
- Error handling with proper HTTP status codes
- ✅ Tested with **Postman**

---

## 🛠️ Tech Stack
- **Python 3.12+**
- **Django**
- **Django REST Framework**
- **Serverless Framework**
- **serverless-wsgi**
- **serverless-offline**

---

> ⚠️ **Note:**  
The `serverless.yml` file is **not included** in this repo because it contains personal Gmail credentials (email & app password).  
If you clone this repo, you’ll need to create your own `serverless.yml` file.

---

### Run this project

## Create a virtual environment
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows

## Install dependencies
    pip install -r requirements.txt

## Configure Environment
    EMAIL_HOST_USER=your-email@gmail.com
    EMAIL_HOST_PASSWORD=your-app-password

## Run Serverless Offline
    sls wsgi serve

## API Usage (with DRF API + Postman)
    http://localhost:5000/api/send-email/

## Request Body (JSON)
    {
        "receiver_email": "receiver@example.com",
        "subject": "Test Email",
        "body_text": "Hello! This is a test email from Django Email API."
    }

## Example Success Response
    {
        "status": "success",
        "message": "Email sent successfully"
    }

## Example Error Response
    {
        "status": "error",
        "message": "Invalid email address"
    }

---

## Snap Shots

### Postman Success
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/3a90878e-8017-4991-831b-d0729e155c42" />

### Gmail
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/5b15403f-1c87-4222-a978-956e751f04ed" />

### Postman Error
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/eeecfd18-de54-485e-836a-8ecbe1a20ee8" />



