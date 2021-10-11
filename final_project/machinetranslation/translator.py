import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version='2018-05-01'

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=version,authenticator=authenticator)
language_translator.set_service_url(url)

en_text = "Hello, world"
fr_text = "Bonjour"

def englishToFrench(englishText):
    frenchText = language_translator.translate(text=englishText, model_id='en-fr').get_result()
    frenchText = frenchText['translations'][0]['translation']
    return frenchText

translated_Fr = englishToFrench(en_text)

def frenchToEnglish(frenchText):
    englishText = language_translator.translate(text=frenchText, model_id='fr-en').get_result()
    englishText= englishText['translations'][0]['translation']
    return englishText

translated_En = frenchToEnglish(fr_text)

#print("en to fr text:",translated_Fr)
#print("fr to en text:",translated_En)