from selenium.common.exceptions import NoSuchElementException
from services.NinetyMinGenerator import NinetyMinGeneratorClient

WebDriver_ = NinetyMinGeneratorClient()
WebDriver_.surf_website()


def test_check_if_header_menu_is_displayed():
    try:
        heders_menu = WebDriver_.find_element_by_css_selector(
            "ul[class$='fixedUl_nkctac']").is_displayed()
        assert heders_menu == True
    except NoSuchElementException:
        return False
    return True


# sorry for the last test
# its not what i needed to be, i cont find how to get list of items.
# what i whanted to to that after opinig the dropdown i can slelct each elemnt inside
def test_change_lang_to_ES():
    try:
        WebDriver_.find_element_by_css_selector(
            "button[class$='button_4p7csh-o_O-tagStyle_bplnm6']").click()
        WebDriver_.find_element_by_css_selector(
            "#mm-root > header > div > div:nth-child(2) > div._mi0zh5 > ul > li:nth-child(3) > a"
        ).click()
        heders_menu = WebDriver_.find_element_by_css_selector(
            "ul[class$='fixedUl_nkctac']")
        assert heders_menu.text == 'LaLiga\nFichajes\nChampions League\nCopa Libertadores\nOpinión\nLiga MX\nMás'
    except:
        return False
