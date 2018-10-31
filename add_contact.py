# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class AddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"

        
    
    def test_add_contact(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/edit.php")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("Pierre")
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys("Nik")
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("Sto")
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys("psto")
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("title")
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys("comp")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("adress")
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys("514")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("515")
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys("516")
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys("517")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("p@gmail.com")
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys("p.com")
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text("18")
        driver.find_element_by_name("bday").click()
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("January")
        driver.find_element_by_name("bmonth").click()
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys("1988")
        driver.find_element_by_name("aday").click()
        Select(driver.find_element_by_name("aday")).select_by_visible_text("16")
        driver.find_element_by_name("aday").click()
        driver.find_element_by_name("amonth").click()
        Select(driver.find_element_by_name("amonth")).select_by_visible_text("February")
        driver.find_element_by_name("amonth").click()
        driver.find_element_by_name("ayear").click()
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys("1989")
        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys("address second")
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys("home second")
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("note")
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        driver.find_element_by_link_text("home").click()
        driver.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
