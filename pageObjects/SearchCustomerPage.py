from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class SearchCustomer:
    # Add customer Page
    txtEmail_id = "SearchEmail"  # "//*[@id='SearchEmail']"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"
    tblSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"# "//*[@id='customers-grid']/tbody/tr"  #
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        # self.driver.find_element_by_id(self.txtEmail_id).clear()
        # self.driver.find_element_by_id(self.txtEmail_id).send_keys(email)

        temail = WebDriverWait(self.driver, 2).until(ec.presence_of_element_located((By.ID, self.txtEmail_id)))
        temail.clear()
        temail.send_keys(email)

    def setFirstName(self, fname):
        # self.driver.find_element_by_id(self.txtFirstName_id).clear()
        # self.driver.find_element_by_id(self.txtFirstName_id).send_keys(fname)

        fName = WebDriverWait(self.driver, 2).until(ec.presence_of_element_located((By.ID, self.txtFirstName_id)))
        fName.clear()
        fName.send_keys(fname)

    def setLastName(self, lname):
        # self.driver.find_element_by_id(self.txtLastName_id).clear()
        # self.driver.find_element_by_id(self.txtLastName_id).send_keys(lname)

        lName = WebDriverWait(self.driver, 2).until(ec.presence_of_element_located((By.ID, self.txtLastName_id)))
        lName.clear()
        lName.send_keys(lname)

    def clickSearch(self):
        # self.driver.find_element_by_id(self.btnSearch_id).click()

        btSearch = WebDriverWait(self.driver, 2).until(ec.presence_of_element_located((By.ID, self.btnSearch_id)))
        btSearch.click()

    def getNoOfRows(self):
        # return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))
        l = self.driver.find_element(by=By.XPATH, value=self.tableRows_xpath).text
        # l = len(WebDriverWait(self.driver, 2).until(ec.presence_of_element_located((By.XPATH, self.tableRows_xpath))))
        print("Number of Rows:", len(l[0]))
        return len(l[0])

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            # table = self.driver.find_element_by_xpath(self.table_xpath)
            table = self.driver.find_element(by=By.XPATH, value=self.table_xpath)
            # emailid = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text
            emailid = table.find_element(by=By.XPATH, value="//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            # table = self.driver.find_element_by_xpath(self.table_xpath)
            table = self.driver.find_element(by=By.XPATH, value=self.table_xpath)
            # name = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            name = table.find_element(by=By.XPATH, value="//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag
