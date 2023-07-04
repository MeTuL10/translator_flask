from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    s=translator.english_to_french(textToTranslate)
    return "Translated text to French: "+s 

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    s=translator.french_to_english(textToTranslate)
    return "Translated text to English: "+s

@app.route("/")
def renderIndexPage():
    render_template("templates\\index.html")
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
