import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('egmSRYgt4t8NEAWRLvE9p0EJgNMtvRhySdOD7Rr46Df3')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/e48a9d50-822d-4252-b130-2200362e2f2c')
def englishToFrench(englishText):
    translation = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    #print(json.dumps(translation, indent=2, ensure_ascii=False))
    #print(translation["translations"][0]["translation"])
    return translation["translations"][0]["translation"]
   

def frenchToEnglish(frenchText):
    translation = language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()
    #print(json.dumps(translation, indent=2, ensure_ascii=False))
    return translation["translations"][0]["translation"]
