# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from add_new_contact import Contact

class AddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.add_user(wd, Contact(firstname="Pierre", middlename="Nik", lastname="Sto", nickname="psto", title="title", company="comp", address="address", homephone="514", mobilephone="515", workphone="516", fax="517",
                      email="p@gmail.com", homepage="p.com", birthday="18", birthmonth="January", birthyear="1988", anniversaryday="16", anniversarymonth="February", anniversaryyear="1989", address_2="address second",
                      phone_2="518", notes="notes"))
        self.submit_specified_user(wd)
        self.go_to_home_page(wd)
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.add_user(wd, Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", homephone="", mobilephone="", workphone="", fax="", email="", homepage="", birthday="-", birthmonth="-", birthyear="", anniversaryday="-", anniversarymonth="-", anniversaryyear="", address_2="", phone_2="", notes=""))
        self.submit_specified_user(wd)
        self.go_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def go_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def submit_specified_user(self, wd):
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def add_user(self, wd, add_new_contact):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(add_new_contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(add_new_contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(add_new_contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(add_new_contact.nickname)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(add_new_contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(add_new_contact.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(add_new_contact.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(add_new_contact.homephone)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(add_new_contact.mobilephone)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(add_new_contact.workphone)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(add_new_contact.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(add_new_contact.email)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(add_new_contact.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(add_new_contact.birthday)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(add_new_contact.birthmonth)
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(add_new_contact.birthyear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(add_new_contact.anniversaryday)
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(add_new_contact.anniversarymonth)
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(add_new_contact.anniversaryyear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(add_new_contact.address_2)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(add_new_contact.phone_2)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(add_new_contact.notes)

    def login(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/edit.php")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()


