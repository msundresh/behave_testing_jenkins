from selenium.webdriver.common.keys import Keys

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.login_button = "//span[contains(text(),'Login')]"
        self.username_textbox = "//input[@name='loginfmt']"
        self.password_textbox = "//input[@name='passwd']"
        self.remeber_password_no_button = "//*[@id='idBtn_Back']"

    def click_login_button(self):
        self.driver.find_element_by_xpath(self.login_button).click()

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username_textbox).send_keys(username)
        self.driver.find_element_by_xpath(self.username_textbox).send_keys(Keys.TAB)
        self.driver.find_element_by_xpath(self.username_textbox).send_keys(Keys.TAB)
        self.driver.find_element_by_xpath(self.username_textbox).send_keys(Keys.TAB)
        self.driver.find_element_by_xpath(self.username_textbox).send_keys(Keys.ENTER)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox).send_keys(password)
        self.driver.find_element_by_xpath(self.password_textbox).send_keys(Keys.TAB)
        self.driver.find_element_by_xpath(self.password_textbox).send_keys(Keys.TAB)
        self.driver.find_element_by_xpath(self.password_textbox).send_keys(Keys.TAB)
        self.driver.find_element_by_xpath(self.password_textbox).send_keys(Keys.ENTER)

    def click_dont_remember_user(self):
        self.driver.find_element_by_xpath(self.remeber_password_no_button).click()