'''importing module'''
from deep_translator import MyMemoryTranslator
def english_to_french(english_text):
    french_text=MyMemoryTranslator("en-IN","fr-FR").translate(english_text)
    return french_text
def french_to_english(french_text):
    english_text=MyMemoryTranslator("fr-FR","en-IN").translate(french_text)
    return english_text
