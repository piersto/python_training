class DelContact:

    def __init__(self, app):
        self.app = app

    def test_untitled_test_case(self):
        driver = self.app.wd
        driver.get("http://localhost/addressbook/")
        driver.find_element_by_id("26").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Select all'])[1]/following::input[2]").click()

    def is_element_present(self, how, what):
        try:
            self.app.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.app.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.app.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True
