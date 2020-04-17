from time import sleep
from ..translator import  Translator

WEBSITE_URL = "https://translate.google.com/"
INPUT_TEXT_CLASS = "tlid-source-text-input"
OUTPUT_TEXT_CLASS = "tlid-translation"

LANGUAGE_ITEM_TEXT_CLASS = "language_list_item_language_name"
OPEN_SOURCE_LANGUAGES_LIST = "tlid-open-source-language-list"
OPEN_TARGET_LANGUAGES_LIST = "tlid-open-target-language-list"

def get_language_list_element(driver, language):
    elements = driver.find_elements_by_xpath(f"//div[contains(@class, 'language-list')]//div[contains(@class, 'language_list_section')]//div[contains(@class, 'language_list_item_wrapper')]//*[contains(text(), '{language}')]")
    element = None

    for e in elements:
        if e.text == language:
            element = e

    return element

class GoogleTranslator(Translator):
    def __init__(self, sleep_request, sleep_reload, sleep_translation=2):
        super().__init__(WEBSITE_URL, INPUT_TEXT_CLASS, OUTPUT_TEXT_CLASS, 5000,
                         sleep_request, sleep_reload, sleep_translation)

    def _get_valid_languages(self):
        elements = self.driver.find_elements_by_class_name(LANGUAGE_ITEM_TEXT_CLASS)
        valid_languages = [element.get_attribute("innerHTML") for element in elements]
        return sorted(list(set(valid_languages)))

    def _set_source_language(self, language):
        element = self.driver.find_element_by_class_name(OPEN_SOURCE_LANGUAGES_LIST)
        element.click()
        sleep(0.5)
        element2 = get_language_list_element(self.driver, language)
        element2.click()

    def _set_target_language(self, language):
        element = self.driver.find_element_by_class_name(OPEN_TARGET_LANGUAGES_LIST)
        element.click()
        sleep(0.5)
        element2 = get_language_list_element(self.driver, language)
        element2.click()