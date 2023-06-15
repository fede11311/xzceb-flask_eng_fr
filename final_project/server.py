"""
Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
"""

import json
from flask import Flask, render_template, request
from machinetranslation import translator


app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    """
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translatedText = translator.englishToFrench(textToTranslate)
    return translatedText

@app.route("/frenchToEnglish")
def frenchToEnglish():
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    """
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translatedText = translator.frenchToEnglish(textToTranslate)
    return translatedText

@app.route("/")
def renderIndexPage():
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    """
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
