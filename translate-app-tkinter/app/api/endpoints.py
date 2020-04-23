from .translators.google_translator import GoogleTranslator
from .translators.deepl_translator import DeeplTranslator

AVALIABLE_SERVICES = {"google translator":GoogleTranslator,
                      "deepl translator":DeeplTranslator}
AVALIABLE_TRANSLATORS = {}


def get_avaliable_services():
    return list(AVALIABLE_SERVICES.keys())


def set_service(name, sleep_request, sleep_reload):
    if name in AVALIABLE_SERVICES:
        AVALIABLE_TRANSLATORS[name] = AVALIABLE_SERVICES[name]()
    else:
        raise Exception(f"Service of name {name} does't exist")


def get_translation_text(service, text, target_language, source_language=None):
    pass