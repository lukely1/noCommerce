from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:
    # Login Page
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"# "//input[@value='Log in']"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        #self.driver.find_element_by_id(self.textbox_username_id).clear()
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(
            (By.ID, self.textbox_username_id))).clear()
        # self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
        userElement = WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(
            (By.ID, self.textbox_username_id)))
        userElement.send_keys(username)

    def setPassword(self, password):
        #self.driver.find_element_by_id(self.textbox_password_id).clear()
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(
            (By.ID, self.textbox_password_id))).clear()
        # self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
        pwdElement = WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(
            (By.ID, self.textbox_password_id)))
        pwdElement.send_keys(password)

    def clickLogin(self):
        #self.driver.find_element_by_xpath(self.button_login_xpath).click()
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(
            (By.XPATH, self.button_login_xpath))).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()
