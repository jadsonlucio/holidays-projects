import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from abc import  abstractmethod, ABC

CHROME_PATH = r'C://Program Files (x86)//Google//Chrome//Application//chrome.exe'
CHROMEDRIVER_PATH = r'drivers//chromedriver.exe'
WINDOW_SIZE = "1920,1080"



class Translator(ABC):
    def __init__(self, website_url, input_text_class, output_text_class, text_size_limit=5000,
                 sleep_request=4, sleep_reload=300, sleep_translation=10, restart_page=10):
        self.website_url = website_url

        self.source_text_class = input_text_class
        self.target_text_class = output_text_class
        self.text_size_limit = 4000

        self.sleep_request = sleep_request
        self.sleep_reload = sleep_reload
        self.sleep_translation = sleep_translation
        self.restart_page = restart_page

        self.driver = self._setup_driver()

        self.text = ""
        self.translated_text = ""
        self._cache_translated_source = ""
        self._cache_translated_target = ""

        self.source_language = ""
        self.target_language = ""
        self.valid_languages = []
        self.callback = lambda translator: print("teste")

        self.setup_website()

    def setup_website(self):
        self.driver.implicitly_wait(20)
        self.driver.get(self.website_url)

    def restart(self):
        self.driver.close()
        self.driver = self._setup_driver()
        self.setup_website()
        self.set_source_language(self.source_language)
        self.set_target_language(self.target_language)

    def save_cache(self, i):
        with open(f"cache/source/{i}.txt", "w", encoding="utf-8") as f:
            f.write(self.text)

        with open(f"cache/target/{i}.txt", "w", encoding="utf-8") as f:
            f.write(self.translated_text)

    def reset_cache(self):
        self._cache_translated_source = ""
        self._cache_translated_target = ""

    def pre_process_text(self, text):
        lines = text.split("\n")
        text_batchs = [""]
        for line in lines:
            if len(line) > self.text_size_limit:
                raise Exception("paragraph can't have the size greater than text_size_limit")
            if len(text_batchs[-1] + line) < self.text_size_limit:
                text_batchs[-1] += line + "\n"
            else:
                text_batchs.append(line)

        return text_batchs

    def translate_text(self, text, target_language=None, source_language=None, save_cache=True):
        self.source_language = source_language
        self.target_language = target_language
        self.reset_cache()

        if target_language:
            if target_language in self.valid_languages:
                self.set_target_language(target_language)
            else:
                raise Exception(f"Language {target_language} is't an valid language")
        if source_language:
            if source_language in self.valid_languages:
                self.set_source_language(source_language)
            else:
                raise Exception(f"Language {target_language} is't an valid language")

        end_point = 498
        cont = 1
        for i, text_batch in enumerate(self.pre_process_text(text)[end_point:]):
            print(text_batch)
            self.callback(self)
            self._translate_text(text_batch)
            if self.restart_page and cont%self.restart_page==0:
                self.restart()
            if save_cache:
                self.save_cache(i+end_point)
            cont+=1

        return self._cache_translated_target

    def _translate_text(self, text):
        element = self.driver.find_element_by_class_name(self.source_text_class)
        element.clear()
        element.send_keys(text)
        sleep(15)
        self.driver.save_screenshot("screenshot.png")
        element2 = self.driver.find_element_by_class_name(self.target_text_class)
        if element2.text == "" or element2.text is None:
            translated_text = element2.get_attribute("value")
        else:
            translated_text = element2.text

        if text.count("[...]") != translated_text.count("[...]") or len(translated_text) < 0.80 * len(text):
            print(f"Entrou sleep por {self.sleep_reload} segundos")
            sleep(self.sleep_reload)

            self._translate_text(text)
        else:
            self.text = text
            self.translated_text = translated_text
            self._cache_translated_source += text
            self._cache_translated_target += translated_text

    def translate_file(self, file_path, target_language=None, save_cache=True, printsreen=True):
        with open(file_path, "r", encoding="utf-8") as f:
            text = "".join(f.readlines())
            translated_text = self.translate_text(text)

        return translated_text

    def set_source_language(self, language):
        self._set_source_language(language)
        self.source_language = language

    def set_target_language(self, language):
        self._set_target_language(language)
        self.target_language = language

    def get_valid_languages(self):
        if not self.valid_languages:
            self.valid_languages = self._get_valid_languages()

        return self.valid_languages

    @abstractmethod
    def _set_source_language(self, language):
        pass

    @abstractmethod
    def _set_target_language(self, language):
        pass

    @abstractmethod
    def _get_valid_languages(self):
        pass

    @staticmethod
    def _setup_driver():
        torexe = os.popen(r'C:\Users\Jadson\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe')
        PROXY = "socks5://localhost:9050"  # IP:PORT or HOST:PORT
        chrome_options = Options()
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        chrome_options.binary_location = CHROME_PATH

        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                                  chrome_options=chrome_options)

        return driver

