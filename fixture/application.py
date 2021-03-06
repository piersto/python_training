from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.delete_contact import DeleteContactHelper
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.delete_contact = DeleteContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def return_to_group_page(self):
            wd = self.wd
            wd.find_element_by_link_text("group page").click()


    def create_group(self, group):
            wd = self.wd
            self.open_groups_page()
            # init group creation
            wd.find_element_by_name("new").click()
            # fill group form
            wd.find_element_by_name("group_name").click()
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(group.name)
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(group.header)
            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(group.footer)
            # submit group creation
            wd.find_element_by_name("submit").click()
            self.return_to_group_page()


    def open_groups_page(self):
            wd = self.wd
            wd.find_element_by_link_text("groups").click()


    def open_home_page(self):
            wd = self.wd
            wd.get("http://localhost/addressbook/")


    def is_element_present(self, how, what):
            try:
                self.wd.find_element(by=how, value=what)
            except NoSuchElementException as e:
                return False
            return True


    def go_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()


    def submit_specified_user(self):
        wd = self.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()


    def add_user(self, add_new_contact):
        wd = self.wd
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


    def open_home_page_edit(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/edit.php")


    def edit_contact(self, updated_first_name):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")
        wd.find_element_by_xpath("//img[@alt='Details']").click()
        wd.find_element_by_name("modifiy").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(updated_first_name)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        wd.find_element_by_link_text("home page").click()



    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True


    def destroy(self):
            self.wd.quit()
