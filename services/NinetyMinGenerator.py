from selenium.webdriver.chrome.webdriver import WebDriver

from Infra.web.WebDriverFactory import WebDriverFactory

from data.configuration import web_config


class NinetyMinGeneratorClient:
    def __init__(self, browser_type="Chrome"):
        self._driver: WebDriver = WebDriverFactory.create(browser_type)

    @property
    def driver(self):
        return self._driver

    def surf_website(self):
        self._driver.get(self.__produce_url_by_environment_type())

    def teardown(self) -> None:
        self._driver.quit()

    def __produce_url_by_environment_type(self) -> str:
        return f"{web_config.base_url}"

    def find_element_by_css_selector(self, css):
        return self._driver.find_element_by_css_selector(css)

    def find_element_by_xpath(self, xpath):
        return self._driver.find_element_by_xpath(xpath)

    def find_elements_by_tag_name(self, tag_name):
        return self._driver.find_elements_by_tag_name(tag_name)
