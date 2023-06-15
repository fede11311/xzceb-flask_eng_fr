"""
Este módulo proporciona funciones para traducir texto entre inglés y francés.

Funciones:
- english_to_french(texto): Traduce texto de inglés a francés.
- frenchToEnglish(texto): Traduce texto de francés a inglés.
"""

from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    #write the code here
    """
    Traduce el texto en inglés al francés.

    :param englishText: El texto en inglés que se desea traducir.
    :type englishText: str
    :return: El texto traducido al francés.
    :rtype: str
    """

    frenchText = MyMemoryTranslator(source='en', target='fr').translate(englishText)

    return frenchText


def frenchToEnglish(frenchText):
    """
    Traduce el texto en francés al inglés.

    :param frenchText: El texto en francés que se desea traducir.
    :type frenchText: str
    :return: El texto traducido al inglés.
    :rtype: str
    """

    englishText = MyMemoryTranslator(source='fr', target='en').translate(frenchText)

    return englishText
