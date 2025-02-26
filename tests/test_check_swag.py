from pages.swag_labs import SwagLabs

def test_find_element1(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    assert swag_labs_page.exist_icon()

def test_find_element2(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    assert swag_labs_page.exist_icon('#user-name')

def test_find_element3(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    assert swag_labs_page.exist_icon('#password')

