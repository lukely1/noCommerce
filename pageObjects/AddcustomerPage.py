import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class AddCustomer:
    # Add customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]" # "//a[@href='#']//span[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary'] " # "//a[@class='btn bg-blue']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    #drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    rdMaleGender_id = "//input[@id='Gender_Male']" #"Gender_Male"
    rdFeMaleGender_id = "//input[@id='Gender_Female']"
    txtFirstName_xpath = "//*[@id='FirstName']" # //input[@id='FirstName']"
    txtLastName_xpath = "//*[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    # taglist_xpath = "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]"
    # click on Customer roll list box
    taglist_xpath = "//div[@class='k-widget k-multiselect k-multiselect-clearable k-state-hover k-state-focused k-state-border-down']//div[@role='listbox']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        #self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()
        WebDriverWait(self.driver, 2).until(ec.presence_of_element_located(
            (By.XPATH, self.lnkCustomers_menu_xpath))).click()

    def clickOnCustomersMenuItem(self):
        self.driver.implicitly_wait(5)
        WebDriverWait(self.driver, 2).until(ec.presence_of_element_located(
            (By.XPATH, self.lnkCustomers_menuitem_xpath))).click()

    def clickOnAddnew(self):
        WebDriverWait(self.driver, 2).until(ec.presence_of_element_located(
            (By.XPATH, self.btnAddnew_xpath))).click()

    def setEmail(self, email):
        #self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)
        txtEmail = WebDriverWait(self.driver, 2).until(ec.presence_of_element_located(
            (By.XPATH, self.txtEmail_xpath)))
        txtEmail.send_keys(email)

    def setPassword(self, password):
        self.driver.implicitly_wait(5)
        txtPwd = WebDriverWait(self.driver, 2).until(ec.presence_of_element_located(
            (By.XPATH, self.txtPassword_xpath)))
        txtPwd.send_keys(password)

    def setCustomerRoles(self, role):
        #self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
        WebDriverWait(self.driver, 2).until(ec.presence_of_element_located(
            (By.XPATH, self.txtcustomerRoles_xpath))).click()
        self.driver.implicitly_wait(5)
        if role == 'Registered':
            #self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
            self.listitem = WebDriverWait(self.driver, 2)\
                .until(ec.presence_of_element_located((By.XPATH, self.lstitemRegistered_xpath)))
        elif role == 'Administrators':
            self.listitem = WebDriverWait(self.driver, 2) \
                .until(ec.presence_of_element_located((By.XPATH, self.lstitemAdministrators_xpath)))
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            # self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            # self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)

            tagList = self.listitem = WebDriverWait(self.driver, 2) \
                .until(ec.presence_of_element_located((By.XPATH, self.taglist_xpath)))
            tagList.click()
            self.listitem = WebDriverWait(self.driver, 2) \
                .until(ec.presence_of_element_located((By.XPATH, self.lstitemGuests_xpath)))
        elif role == 'Registered':
            # self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
            self.listitem = WebDriverWait(self.driver, 2) \
                .until(ec.presence_of_element_located((By.XPATH, self.lstitemRegistered_xpath)))
        elif role == 'Vendors':
            # self.listitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
            self.listitem = WebDriverWait(self.driver, 2) \
                .until(ec.presence_of_element_located((By.XPATH, self.lstitemVendors_xpath)))
        else:
            # self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
            self.listitem = WebDriverWait(self.driver, 2) \
                .until(ec.presence_of_element_located((By.XPATH, self.lstitemGuests_xpath)))
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        self.driver.implicitly_wait(2)
        # drp = Select(self.driver.find_element_by_xpath(self.drpmgrOfVendor_xpath))
        drp = Select(WebDriverWait(self.driver, 2).until(ec.presence_of_element_located((By.XPATH, self.drpmgrOfVendor_xpath))))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        self.driver.implicitly_wait(2)
        if gender == 'Male':
            WebDriverWait(self.driver, 2).until(ec.presence_of_element_located(
                (By.XPATH, self.rdMaleGender_id))).click()
            # self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender == 'Female':
            WebDriverWait(self.driver, 2).until(ec.presence_of_element_located(
                (By.XPATH, self.rdFeMaleGender_id))).click()
            #self.driver.find_element_by_id(self.rdFeMaleGender_id).click()
        else:
            WebDriverWait(self.driver, 2).until(ec.presence_of_element_located(
                (By.XPATH, self.rdFeMaleGender_id))).click()
            #Fself.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.implicitly_wait(2)
        fName = WebDriverWait(self.driver, 2).until(ec.presence_of_element_located(
            (By.XPATH, self.txtFirstName_xpath)))
        fName.send_keys(fname)
        #self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.implicitly_wait(2)
        lstName = WebDriverWait(self.driver, 2).until(ec.presence_of_element_located(
            (By.XPATH, self.txtLastName_xpath)))
        lstName.send_keys(lname)
        #self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.implicitly_wait(2)
        dob1 = WebDriverWait(self.driver, 2).until(ec.presence_of_element_located(
            (By.XPATH, self.txtDob_xpath)))
        dob1.send_keys(dob)
        #self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        comName = WebDriverWait(self.driver, 2).until(ec.presence_of_element_located(
            (By.XPATH, self.txtCompanyName_xpath)))
        comName.send_keys(comname)
        # self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        con = WebDriverWait(self.driver, 2).until(ec.presence_of_element_located(
            (By.XPATH, self.txtAdminContent_xpath)))
        con.send_keys(content)
        #self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.implicitly_wait(2)
        WebDriverWait(self.driver, 2).until(ec.presence_of_element_located(
            (By.XPATH, self.btnSave_xpath))).click()
        #self.driver.find_element_by_xpath(self.btnSave_xpath).click()
