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

AFFILIATE_ADS = [
    {
        "title": "Truesearch",
        "link": "https://true-search.io/",
        "heading": "The Charitable Works 1",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae voluptates aspernatur maxime nesciunt obcaecati",
        "more_links": [
            {
                "title": "Wishtree",
                "link": "https://wishtreetech.com/"
            },
            {
                "title": "Truesearch",
                "link": "https://true-search.ai/"
            }
        ]
    },
    {
        "title": "Truesearch",
        "link": "https://true-search.io/",
        "heading": "The Charitable Works 2",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae voluptates aspernatur maxime nesciunt obcaecati",
        "more_links": [
            {
                "title": "Wishtree",
                "link": "https://wishtreetech.com/"
            },
            {
                "title": "Truesearch",
                "link": "https://true-search.ai/"
            }
        ]
    },
    {
        "title": "Truesearch",
        "link": "https://true-search.io/",
        "heading": "The Charitable Works 3",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae voluptates aspernatur maxime nesciunt obcaecati",
        "more_links": [
            {
                "title": "Wishtree",
                "link": "https://wishtreetech.com/"
            },
            {
                "title": "Truesearch",
                "link": "https://true-search.ai/"
            }
        ]
    }
]