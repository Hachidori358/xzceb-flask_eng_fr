""""
translates between French and English
"""
from deep_translator import MyMemoryTranslator
from flask import Flask, request

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    """
    Translates English to French
    """
    text_to_translate = request.args.get('textToTranslate')
    translator = MyMemoryTranslator(source='en', target='fr')
    translated_text = translator.translate(text_to_translate)
    return f"Translated text to French: {translated_text}"

@app.route("/frenchToEnglish")
def french_to_english():
    """
    Translates French to English
    """
    text_to_translate = request.args.get('textToTranslate')
    translator = MyMemoryTranslator(source='fr', target='en')
    translated_text = translator.translate(text_to_translate)
    return f"Translated text to English: {translated_text}"

if __name__ == '__main__':
    app.run()
