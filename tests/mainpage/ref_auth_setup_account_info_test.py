import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote


from steps.auth.auth_steps import AuthSteps
from steps.mainpage.main_page_steps import MainSteps
from tests.base_test import BaseTest


class RefAuthSetupAccountInfoTest(BaseTest):

    def test(self):
        driver = self.driver

        mainsteps = MainSteps(driver)
        mainsteps.open()
        mainsteps.button_signin()
        driver.switch_to.frame(driver.find_element_by_css_selector('[class="ag-popup__frame__layout__iframe"]'))

        AuthSteps(driver).auth_main_page()

        mainsteps_after_auth = MainSteps(driver)
        mainsteps_after_auth.ref_auth_main_button()
        mainsteps_after_auth.ref_auth_setup_account_info()

        assert "No results found." not in driver.page_source
