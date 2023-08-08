import os
from dotenv import load_dotenv

load_dotenv()

SMTP_DATA = {
    "host": "smtp.office365.com", 
    "port": 587, #STARTTLS Port - 25, 587 or 2587
    "timeout": 30,
    "user": "postmaster@true-search.io",
    "password": os.getenv('SMTP_PASS'),
    "tls":True,
}

TO_MAIL = ['roszellmc@protonmail.com']
SUBJECT = "Feedback"