import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from pages.profile.profile import ProfilePage
from steps.auth.auth_steps import AuthSteps
from steps.profile.profile_steps import ProfileSteps
from tests.base_test import BaseTest


class EmptyTest(BaseTest):
    NAME = ""
    ERROR = 'Укажите имя'


    def test(self):
        driver = self.driver
        AuthSteps(driver).auth()

        profile_steps = ProfileSteps(self.driver)
        profile_steps.open()
        profile_steps.set_name(self.NAME)
        profile_steps.save()

        self.assertEqual(self.ERROR, profile_steps.empty_name_error())
