from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)


    def logout(self):
            wd = self.wd
            wd.find_element_by_link_text("Logout").click()


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


    def login(self, username, password):
            wd = self.wd
            self.open_home_page()
            wd.find_element_by_name("user").click()
            wd.find_element_by_name("user").clear()
            wd.find_element_by_name("user").send_keys(username)
            wd.find_element_by_name("pass").clear()
            wd.find_element_by_name("pass").send_keys(password)
            wd.find_element_by_xpath("//input[@value='Login']").click()


    def open_home_page(self):
            wd = self.wd
            wd.get("http://localhost/addressbook/")


    def is_element_present(self, how, what):
            try:
                self.wd.find_element(by=how, value=what)
            except NoSuchElementException as e:
                return False
            return True


    def destroy(self):
            self.wd.quit()
