from machinetranslation import translator
from flask import Flask, render_template, request
import json

import machinetranslation

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    text_to_translate = request.args.get('textToTranslate')
    translated_text = translate(text_to_translate, 'fr')
    return f"Translated text to French: {translated_text}"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    text_to_translate = request.args.get('textToTranslate')
    translated_text = translate(text_to_translate, 'en')
    return f"Translated text to English: {translated_text}"

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
