import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests

nest_username = ""
nest_password = ""
webhook_url =  ""

class NestPension:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        self.driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), chrome_options=chrome_options)
        self.driver.get("https://www.nestpensions.org.uk/schemeweb/NestWeb/faces/public/MUA/pages/loginPage.xhtml")

    def login(self):
        user_field = self.driver.find_element_by_id("username")
        user_field.clear()
        user_field.send_keys(nest_username)

        pass_field = self.driver.find_element_by_id("password")
        pass_field.clear()
        pass_field.send_keys(nest_password)

        login_button = self.driver.find_element_by_name("lockLnk12")
        login_button.click()

        return self.driver

    def potbreakdown(self):
        self.driver.get("https://www.nestpensions.org.uk/schemeweb/NestWeb/faces/secure/FE/pages/fundValueReport.xhtml")
        self.no_of_units = self.driver.find_element_by_xpath("//td[@class='header2']//span[@class='paymentHistoryAmt']").text
        self.unit_price = self.driver.find_element_by_xpath("//td[@class='header3']//span[@class='paymentHistoryAmt']").text
        self.fund_value = self.driver.find_element_by_xpath("//td[@class='header4']//span[@class='paymentHistoryAmt']").text
        return

    def addtorecord(self):
        report = {}
        report["value1"] = self.no_of_units
        report["value2"] = self.unit_price
        report["value3"] = self.fund_value
        requests.post(webhook_url, data=report)
        return

    def closesession(self):
        self.driver.quit()
        return

Session = NestPension()
Session.login()
Session.potbreakdown()
Session.addtorecord()
Session.closesession()
