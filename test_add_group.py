# -*- coding: utf-8 -*-
from selenium import webdriver

import unittest

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_page_group(wd)
        self.init_group_creation(wd)
        self.fill_group_form(wd)
        self.submit_group_creation(wd)
        self.return_to_groups_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def submit_group_creation(self, wd):
        wd.find_element_by_name("submit").click()

    def fill_group_form(self, wd):
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("Group 1")
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("group 1 -1")
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("group1-1-1")

    def init_group_creation(self, wd):
        wd.find_element_by_name("new").click()

    def open_page_group(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
