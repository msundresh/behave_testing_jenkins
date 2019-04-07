from selenium import  webdriver

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.burger_navigate_icon = "//span[@class='burger-nav-icon-parent']"
        self.customer_management_tab = "//span[contains(text(),'CUSTOMER MANAGEMENT')]"
        self.create_new_customer_button = "//*[contains(text(),'Add New Customer')]"

    def click_burger_navigate_icon(self):
        self.driver.find_element_by_xpath(self.burger_navigate_icon).click()

    def click_customer_management_tab(self):
        self.driver.find_element_by_xpath(self.customer_management_tab).click()

    def click_add_customer_button(self):
        self.driver.find_element_by_xpath(self.create_new_customer_button).click()