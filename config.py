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

BLACKLIST = {
    "mymortgagefreedom.com.au", "moneyquest.com.au", "rdfg.com.au", 
    "ufinancial.com.au", "marketstreetfinance.com.au", 
    "bespokefinancialadvisory.com.au", "itssimple.com.au", 
    "blueowl.com", "bluecherryloans.com.au", "thrivingwealth.com.au", 
    "propertytwins.com.au", "btlnet.com", "beautyaffairs.com.au", 
    "erase.com.au", "drcosima.com.au", "dntlcode.com.au", "zurich.com.au", 
    "aussie.com.au", "mortgagechoice.com.au", "bdo.com.au", 
    "grantthornton.com.au", "kokodaproperty.com.au", "pitcher.com.au", 
    "freedompropertyinvestors.com.au", "rocconsulting.com", "sgua.com.au", 
    "nicheadvisory.com.au", "finradvisory.com.au", "alliancecorp.com.au", 
    "aipt.edu.au", "jrprosperity.com.au", "thebeautytechgroup.com", 
    "thirsty.group", "tal.com.au", "itssimple.com.au", "moneyquest.com.au", 
    "btlnet.com", "drcosima.com.au", "venuspack.com.au", "bodywrl.com.au", 
    "grpaustralia.com.au", "ultimate.net.au", "freshstartadvisory.com.au", 
    "charterprivate.com.au", "ufinancial.com.au", "asahibeverages.com", 
    "crosscarendis.com.au", "erase.com.au", "ethicalinvestments.com.au", 
    "bluecherryloans.com.au", "indigofinance.com.au", "jabsonsfinance.com.au", 
    "rdfg.com.au", "primeplatinum.com", "ridgemontpartners.com.au", 
    "ikaya.com.au", "parityconsulting.com.au", "ethosmigration.com.au", 
    "dymocks.com.au", "atlaspropertygroup.com.au", "investorkit.com.au", 
    "lifeinsurancepartners.com.au", "orangelegalgroup.com.au", 
    "designerjourneys.com", "imintheright.com.au", "paliseproperty.com", 
    "opencorp.com.au", "mgiadelaide.com.au", "digcapitaladvisory.com", 
    "australconstruction.com.au", "lunainc.com", "greenrockadvisory.com.au", 
    "neilsonfs.com", "finance4nurses.com.au", "resolvefinance.com.au"
}

VALID_TITLES = {
    "sale", "business development", "account", "success", "lead", "telemarketer"
}

INVALID_TITLES = {
    "retail", "vehicle", "car", "realestate", "automotive", "casual"
}