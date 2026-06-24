import os

from dotenv import load_dotenv

load_dotenv()

SMARTLEAD_API_KEY = os.getenv("SMARTLEAD_API_KEY")
LEAD_MAGIC_KEY = os.getenv("LEAD_MAGIC_KEY")
AI_API_KEY = os.getenv("AI_API_KEY")
APIFY_API_KEY = os.getenv("APIFY_API_KEY")

MULTI_PART_TLDS = {
    'com.au', 'gov.au', 'net.au', 'edu.au', 'org.au'
}