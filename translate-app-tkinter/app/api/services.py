from .translators.google_translator import GoogleTranslator
from .translators.deepl_translator import DeeplTranslator

AVALIABLE_SERVICES = {"google translator": GoogleTranslator,
                      "deepl translator": DeeplTranslator}


class ServiceManager:
    def __init__(self):
        self.avaliable_translators = {}

    def set_service(self, service_name, sleep_request, sleep_reload, sleep_translation=None):
        if service_name in AVALIABLE_SERVICES:
            if service_name not in self.avaliable_translators:
                if sleep_translation:
                    translator = AVALIABLE_SERVICES[service_name](sleep_request, sleep_reload, sleep_translation)
                else:
                    translator = AVALIABLE_SERVICES[service_name](sleep_request, sleep_reload)
                self.avaliable_translators[service_name] = translator
        else:
            raise Exception(f"Service of name {service_name} does't exist")

    def get_translator(self, service_name):
        if service_name not in self.avaliable_translators:
            raise Exception(f"Service of {service_name} don't setted, please use set_service")

        return self.avaliable_translators[service_name]

    @staticmethod
    def get_avaliable_services():
        return list(AVALIABLE_SERVICES.keys())

