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

AD_ROTATE_TIME = 15 #Time in seconds for affiliate ads rotation
AFFILIATE_ADS = [
    {
        "title": "Save 10% today at our affiliate bookstores",
        "link": "https://true-search.io/"
    },
    {
        "title": "Save 12% today at our affiliate bookstores",
        "link": "https://true-search.io/"
    },
    {
        "title": "Save 5% today at our affiliate bookstores",
        "link": "https://true-search.io/"
    }
]

CHARITY_LIST = ["American Red Cross", "Habitat for Humanity", "New York Supportive Housing"]
DEFAULT_CHARITY = "American Red Cross"