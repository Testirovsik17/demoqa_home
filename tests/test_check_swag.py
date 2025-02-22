from pages.swag_labs import SwagLabs

def test_find_element(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    assert swag_labs_page.exist_icon('#user-name')
    assert swag_labs_page.exist_icon('#password')
