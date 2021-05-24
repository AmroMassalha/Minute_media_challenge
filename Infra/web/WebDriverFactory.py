from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options

from data.configuration import web_config


class WebDriverFactory:
    @staticmethod
    def create(browser_type="Chrome") -> WebDriver:
        if browser_type == "Chrome":
            return WebDriverFactory._produce_chrome_webdriver()
        raise AttributeError(
            f"The requested '{browser_type}' browser type is not supported.")

    @staticmethod
    def _produce_chrome_webdriver() -> WebDriver:
        chrome_options = Options()
        chrome_options.binary_location = web_config.binary_location
        chrome_options = WebDriverFactory.__set_chromeOptions_arguments(
            chrome_options)
        chrome_options = WebDriverFactory.__add_preferences_to_chromeOptions_as_experimental_option(
            chrome_options)
        chrome_options.set_capability("loggingPrefs", {"browser": "ALL"})
        return webdriver.Chrome(web_config.executable_path,
                                options=chrome_options)

    @staticmethod
    def __set_chromeOptions_arguments(chrome_options) -> Options:
        args = [
            "--ignore-certificate-errors",
            "--incognito",
            "--disable-extensions",
            "--disable-default-apps",
        ]
        [chrome_options.add_argument(arg) for arg in args]
        chrome_options.add_argument("--start-maximized")
        return chrome_options

    @staticmethod
    def __add_preferences_to_chromeOptions_as_experimental_option(
            chrome_options: Options) -> Options:
        prefs = {
            "plugins.plugins_disabled": "Chrome PDF Viewer",
            "credentials_enable_service": "false",
            "profile.password_manager_enabled": "false",
            "profile.default_content_settings.popups": 0,
            "download.prompt_for_download": "false",
            "enableNetwork": "true"
        }
        chrome_options.add_experimental_option("prefs", prefs)
        return chrome_options
