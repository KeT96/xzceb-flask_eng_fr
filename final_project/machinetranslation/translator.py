import os
import json
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version='2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=version,authenticator=authenticator)
language_translator.set_service_url(url)

EN_TEXT = "Hello, world" #testing text
FR_TEXT = "Bonjour" #testing text

def english_to_french(english_text):
    french_text = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = french_text['translations'][0]['translation']
    return french_text

translated_fr = english_to_french(EN_TEXT)

def french_to_english(french_text):
    english_text = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text= english_text['translations'][0]['translation']
    return english_text

translated_en = french_to_english(FR_TEXT)

#print("en to fr text:",translated_fr)
#print("fr to en text:",translated_en)
