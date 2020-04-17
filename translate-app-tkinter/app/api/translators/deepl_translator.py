from time import sleep
from ..translator import  Translator

WEBSITE_URL = "https://www.deepl.com/translator"
INPUT_TEXT_CLASS = "lmt__source_textarea"
OUTPUT_TEXT_CLASS = "lmt__target_textarea"
LANGUAGE_ITEM_TEXT_CLASS = "lmt__language_select__menu"

class DeeplTranslator(Translator):
    def __init__(self, sleep_request, sleep_reload, sleep_translation=10):
        super().__init__(WEBSITE_URL, INPUT_TEXT_CLASS, OUTPUT_TEXT_CLASS, 5000,
                         sleep_request, sleep_reload, sleep_translation)

    def _get_valid_languages(self):
        elements = self.driver.find_elements_by_xpath("//button[@dl-lang]")
        valid_languages = sorted(list(set([elem.get_attribute("innerHTML") for elem in elements])))
        valid_languages.remove("Any language (detect)")
        return valid_languages

    def _set_source_language(self, language):
        element3 = self.driver.find_elements_by_class_name("lmt__language_select__active")[0]
        element3.click()
        sleep(1)
        element4 = self.driver.find_element_by_xpath(f"//div[@dl-test='translator-source-lang-list']//button[text()='{language}']")
        element4.click()

    def _set_target_language(self, language):
        element3 = self.driver.find_elements_by_class_name("lmt__language_select__active")[1]
        element3.click()
        sleep(1)
        element4 = self.driver.find_element_by_xpath("//div[@dl-test='translator-target-lang-list']")
        element4 = element4.find_element_by_xpath(f"//button[text()='{language}']")
        print(element4)
        element4.click()