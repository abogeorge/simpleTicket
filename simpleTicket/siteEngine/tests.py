from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from . import entities_utils
import unittest, time, re
import time

class SiteEngineTests(StaticLiveServerTestCase):

    id_ticket = 22
    id_order = 19

    fixtures = ['user-data.json']

    # --- Set Up and Tear Down Methods ---
    # Set Up
    @classmethod
    def setUpClass(cls):
        super(SiteEngineTests, cls).setUpClass()
        cls.driver = webdriver.Chrome()
        print ("Initialized Chrome Driver ... ")

    # Tear Down
    @classmethod
    def tearDownClass(cls):
        print (" ... Destroying Resources")
        #cls.driver.quit()
        super(SiteEngineTests, cls).tearDownClass()

    # --- Utility methods ---
    # Returns True if an element is identified
    def __is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    # Returns True if the text is identified
    def __is_text_present(self, text):
        values = self.driver.find_elements_by_xpath("//*[contains(text(), '" + text + "')]")
        if len(values) > 0:
            return True
        else:
           return False

    # --- Test Methods ---
    # Test successful Login
    def test1_login(self):
        print ("Testing user login ... ")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/home/login/")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys('george.r')
        password_input = driver.find_element_by_name("password")
        password_input.send_keys('rgeotest123')
        driver.find_element_by_name('Submit').click()
        # Asserting True index page text
        self.assertTrue(self.__is_text_present("simpleTicket is a new self-service app that uses"))
        # Asserting False auth error message
        self.assertFalse(self.__is_text_present("Invalid Username or Password provided! Please try again!"))
        # Asserting True index page element
        self.assertTrue(self.__is_element_present("name", "our-services"))

    # Test unsuccessful Login
    def test2_bad_login(self):
        print ("Testing wrong password user login ... ")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/home/login/")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys('george.r')
        password_input = driver.find_element_by_name("password")
        password_input.send_keys('bad_password')
        driver.find_element_by_name('Submit').click()
        # Asserting True auth error message
        self.assertTrue(self.__is_text_present("Invalid Username or Password provided! Please try again!"))
        # Asserting False index page text
        self.assertFalse(self.__is_text_present("simpleTicket is a new self-service app that uses"))

    # Test Index/Logout
    def test3_logout(self):
        print ("Testing user logout ... ")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/home/login/")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys('george.r')
        password_input = driver.find_element_by_name("password")
        password_input.send_keys('rgeotest123')
        driver.find_element_by_name('Submit').click()
        # Asserting True index page text
        self.assertTrue(self.__is_text_present("simpleTicket is a new self-service app that uses"))
        driver.find_element_by_name('logout').click()
        # Asserting True logout page text
        self.assertTrue(self.__is_text_present("You Have Successfully Logged out of simpleTicket!"))

    # Test Index/MyAccount
    def test4_myaccount(self):
        print ("Testing user MyAccount ... ")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/home/login/")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys('george.r')
        password_input = driver.find_element_by_name("password")
        password_input.send_keys('rgeotest123')
        driver.find_element_by_name('Submit').click()
        # Asserting True index page text
        self.assertTrue(self.__is_text_present("simpleTicket is a new self-service app that uses"))
        driver.find_element_by_name('myaccount').click()
        # Asserting True MyAccount page text information
        self.assertTrue(self.__is_text_present("Personal Information"))
        self.assertTrue(self.__is_text_present("George"))
        self.assertTrue(self.__is_text_present("Rus"))
        self.assertTrue(self.__is_text_present("Cornel Popescu"))

    # Test Index/Services
    def test5_services(self):
        print ("Testing user Services ... ")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/home/login/")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys('george.r')
        password_input = driver.find_element_by_name("password")
        password_input.send_keys('rgeotest123')
        driver.find_element_by_name('Submit').click()
        # Asserting True index page text
        self.assertTrue(self.__is_text_present("simpleTicket is a new self-service app that uses"))
        driver.find_element_by_name('services').click()
        # Asserting True Services page text information
        self.assertTrue(self.__is_text_present("Create Ticket"))
        self.assertTrue(self.__is_text_present("Create a new Ticket"))
        self.assertTrue(self.__is_text_present("If you need any assistance while creating an IT Ticket or placing any kind of order please contact our HelpDesk team."))

    # Test Index/Contact
    def test6_contact(self):
        print ("Testing user Contact ... ")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/home/login/")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys('george.r')
        password_input = driver.find_element_by_name("password")
        password_input.send_keys('rgeotest123')
        driver.find_element_by_name('Submit').click()
        # Asserting True index page text
        self.assertTrue(self.__is_text_present("simpleTicket is a new self-service app that uses"))
        driver.find_element_by_name('contact').click()
        # Asserting True Contact page text information
        self.assertTrue(self.__is_text_present("Contact the HelpDesk Team"))
        self.assertTrue(self.__is_text_present("Send an e-mail"))

    # Test LogIn user/Index/Services/Create Ticket
    def test7_user_create_ticket(self):
        print ("Testing user create ticket ... ")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/home/login/")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys('cristina.g')
        password_input = driver.find_element_by_name("password")
        password_input.send_keys('gcritest123')
        driver.find_element_by_name('Submit').click()
        # Asserting True index page text
        self.assertTrue(self.__is_text_present("simpleTicket is a new self-service app that uses"))
        driver.find_element_by_name('services').click()
        # Asserting True Services page text information
        self.assertTrue(self.__is_text_present("Create Ticket"))
        driver.find_element_by_name('create_ticket').click()
        # Asserting True Create Ticket page text information
        self.assertTrue(self.__is_text_present("Create a Ticket"))
        # Populating form inputs
        category_select = Select(driver.find_element_by_id('type'))
        category_select.select_by_visible_text('Software Problem')
        title_input = driver.find_element_by_name("title")
        title_input.send_keys('Office License')
        description_input = driver.find_element_by_name("description")
        description_input.send_keys('MS 2010 Office license has expired.')
        priority_select = Select(driver.find_element_by_id('priority'))
        priority_select.select_by_visible_text('Medium Priority')
        driver.find_element_by_name('submit').click()
        # Asserting True confirmation message
        self.assertTrue(self.__is_text_present("Ticket successfully created! You will be contacted as soon as possible."))

    # Test LogIn user/Index/Services/Active Tickets
    def test8_user_active_tickets(self):
        print ("Testing user active tickets ... ")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/home/login/")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys('cristina.g')
        password_input = driver.find_element_by_name("password")
        password_input.send_keys('gcritest123')
        driver.find_element_by_name('Submit').click()
        # Asserting True index page text
        self.assertTrue(self.__is_text_present("simpleTicket is a new self-service app that uses"))
        driver.find_element_by_name('services').click()
        # Asserting True Services page text information
        self.assertTrue(self.__is_text_present("Create Ticket"))
        driver.find_element_by_name('active_tickets').click()
        # Asserting True Open Tickets page text information
        self.assertTrue(self.__is_text_present("Active Tickets for Cristina George"))
        self.assertTrue(self.__is_text_present("Office License"))
        self.assertTrue(self.__is_text_present("MS 2010 Office license has expired."))
        self.assertTrue(self.__is_text_present("Medium"))
        self.assertTrue(self.__is_text_present("Sent"))

    # Test LogIn user/Index/Services/Create Order
    def test9_user_create_order(self):
        print ("Testing user create order ... ")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/home/login/")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys('cristina.g')
        password_input = driver.find_element_by_name("password")
        password_input.send_keys('gcritest123')
        driver.find_element_by_name('Submit').click()
        # Asserting True index page text
        self.assertTrue(self.__is_text_present("simpleTicket is a new self-service app that uses"))
        driver.find_element_by_name('services').click()
        # Asserting True Services page text information
        self.assertTrue(self.__is_text_present("Create Ticket"))
        driver.find_element_by_name('create_order').click()
        # Asserting True Create Ticket page text information
        self.assertTrue(self.__is_text_present("Place an Order"))
        # Populating form inputs
        category_select = Select(driver.find_element_by_id('type'))
        category_select.select_by_visible_text('Inventory Item')
        title_input = driver.find_element_by_name("title")
        title_input.send_keys('Desk Lamp')
        description_input = driver.find_element_by_name("description")
        description_input.send_keys('Improve office lighting')
        value_input = driver.find_element_by_name("value")
        value_input.send_keys('69')
        units_input = driver.find_element_by_name("units")
        units_input.send_keys('1')
        delivery_office_input = driver.find_element_by_name("delivery_office")
        delivery_office_input.send_keys('ERO201')
        priority_select = Select(driver.find_element_by_id('priority'))
        priority_select.select_by_visible_text('Medium Priority')
        driver.find_element_by_name('submit').click()
        # Asserting True confirmation message
        self.assertTrue(self.__is_text_present("Order successfully created! You will be contacted as soon as possible."))

    # Test LogIn user/Index/Services/Active Orders
    def test10_user_active_orders(self):
        print ("Testing user active orders ... ")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/home/login/")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys('cristina.g')
        password_input = driver.find_element_by_name("password")
        password_input.send_keys('gcritest123')
        driver.find_element_by_name('Submit').click()
        # Asserting True index page text
        self.assertTrue(self.__is_text_present("simpleTicket is a new self-service app that uses"))
        driver.find_element_by_name('services').click()
        # Asserting True Services page text information
        self.assertTrue(self.__is_text_present("Create Ticket"))
        driver.find_element_by_name('active_orders').click()
        # Asserting True Open Orders page text information
        self.assertTrue(self.__is_text_present("Active Orders for Cristina George"))
        self.assertTrue(self.__is_text_present("Desk Lamp"))
        self.assertTrue(self.__is_text_present("Improve office lighting"))
        self.assertTrue(self.__is_text_present("69.00"))
        self.assertTrue(self.__is_text_present("1"))
        self.assertTrue(self.__is_text_present("Medium"))
        self.assertTrue(self.__is_text_present("Sent"))

    # Test LogIn supervisor/Index/Services/Subordinates
    def test11_supervisor_subordinates(self):
        print ("Testing supervisor subordinates view ... ")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/home/login/")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys('george.r')
        password_input = driver.find_element_by_name("password")
        password_input.send_keys('rgeotest123')
        driver.find_element_by_name('Submit').click()
        # Asserting True index page text
        self.assertTrue(self.__is_text_present("simpleTicket is a new self-service app that uses"))
        driver.find_element_by_name('services').click()
        # Asserting True Services page text information
        self.assertTrue(self.__is_text_present("Manage staff members"))
        driver.find_element_by_name('subalterns').click()
        # Asserting True subordinates page text information
        self.assertTrue(self.__is_text_present("Active subalterns for George Rus"))
        self.assertTrue(self.__is_text_present("Cristina George"))
        self.assertTrue(self.__is_text_present("cristina.george@ticket.com"))
        self.assertTrue(self.__is_text_present("770"))
        self.assertTrue(self.__is_text_present("PDOM-DS"))

        # Test LogIn supervisor/Index/Services/Subordinates

    # Test LogIn supervisor/Index/Services/ApproveTickets
    def test12_supervisor_approve_tickets(self):
        print ("Testing supervisor approve tickets ... ")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/home/login/")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys('george.r')
        password_input = driver.find_element_by_name("password")
        password_input.send_keys('rgeotest123')
        driver.find_element_by_name('Submit').click()
        # Asserting True index page text
        self.assertTrue(self.__is_text_present("simpleTicket is a new self-service app that uses"))
        driver.find_element_by_name('services').click()
        # Asserting True Services page text information
        self.assertTrue(self.__is_text_present("Manage staff members"))
        driver.find_element_by_name('approve_tickets').click()
        # Asserting True subordinates tickets page text information
        self.assertTrue(self.__is_text_present("Tickets pending the approval of George Rus"))
        self.assertTrue(self.__is_text_present("Cristina George"))
        self.assertTrue(self.__is_text_present("Office License"))
        self.assertTrue(self.__is_text_present("MS 2010 Office license has expired."))
        self.assertTrue(self.__is_text_present("Medium"))
        self.assertTrue(self.__is_text_present("Sent"))
        # Opening active ticket
        driver.find_element_by_name(str(self.id_ticket)).click()
        self.assertTrue(self.__is_text_present("Ticket Information"))
        self.assertTrue(self.__is_text_present("Cristina George"))
        self.assertTrue(self.__is_text_present("Office License"))
        # Approving Ticket
        status_select = Select(driver.find_element_by_id('status'))
        status_select.select_by_visible_text('Approved')
        title_comments = driver.find_element_by_name("comments")
        title_comments.send_keys('Ok')
        driver.find_element_by_name('submit').click()
        # Asserting True confirmation message
        self.assertTrue(self.__is_text_present("You have successfully updated the ticket status!"))
        # Asseting that the previous approve ticket is now removed from list
        driver.get("http://127.0.0.1:8000/home/subalterns_tickets/")
        self.assertFalse(self.__is_text_present("Office License"))
        self.assertFalse(self.__is_text_present("MS 2010 Office license has expired."))

        # Test LonIn supervisor/Index/Services/ApproveTickets

    # Test LogIn supervisor/Index/Services/ApproveOrders
    def test13_supervisor_approve_orders(self):
        print ("Testing supervisor approve orders ... ")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/home/login/")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys('george.r')
        password_input = driver.find_element_by_name("password")
        password_input.send_keys('rgeotest123')
        driver.find_element_by_name('Submit').click()
        # Asserting True index page text
        self.assertTrue(self.__is_text_present("simpleTicket is a new self-service app that uses"))
        driver.find_element_by_name('services').click()
        # Asserting True Services page text information
        self.assertTrue(self.__is_text_present("Manage staff members"))
        driver.find_element_by_name('approve_orders').click()
        # Asserting True subordinates orders page text information
        self.assertTrue(self.__is_text_present("Orders pending the approval of George Rus"))
        self.assertTrue(self.__is_text_present("Desk Lamp"))
        self.assertTrue(self.__is_text_present("Improve office lighting"))
        self.assertTrue(self.__is_text_present("Medium"))
        self.assertTrue(self.__is_text_present("Sent"))
        # Opening active order
        driver.find_element_by_name(str(self.id_order)).click()
        self.assertTrue(self.__is_text_present("Order Information"))
        self.assertTrue(self.__is_text_present("Desk Lamp"))
        self.assertTrue(self.__is_text_present("Improve office lighting"))
        # Approving Order
        status_select = Select(driver.find_element_by_id('status'))
        status_select.select_by_visible_text('Approved')
        title_comments = driver.find_element_by_name("comments")
        title_comments.send_keys('Ok')
        driver.find_element_by_name('submit').click()
        # Asserting True confirmation message
        self.assertTrue(self.__is_text_present("You have successfully updated the order status!"))
        # Asseting that the previous approve ticket is now removed from list
        driver.get("http://127.0.0.1:8000/home/subalterns_orders/")
        self.assertFalse(self.__is_text_present("Desk Lamp"))

    # Test LogIn HelpDesk/Index/Services/Employees
    def test14_helpdesk_employees(self):
        print ("Testing supervisor subordinates view ... ")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/home/login/")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys('gigi.h')
        password_input = driver.find_element_by_name("password")
        password_input.send_keys('hgigtest123')
        driver.find_element_by_name('Submit').click()
        # Asserting True index page text
        self.assertTrue(self.__is_text_present("simpleTicket is a new self-service app that uses"))
        driver.find_element_by_name('services').click()
        # Asserting True Services page text information
        self.assertTrue(self.__is_text_present("View contact info for all employees"))
        driver.find_element_by_name('employees_list').click()
        # Asserting True employee page text information
        self.assertTrue(self.__is_text_present("Company Employees"))
        self.assertTrue(self.__is_text_present("Cristina George"))
        self.assertTrue(self.__is_text_present("cristina.george@ticket.com"))
        self.assertTrue(self.__is_text_present("770"))
        self.assertTrue(self.__is_text_present("George Rus"))
        self.assertTrue(self.__is_text_present("george.rus@ticket.com"))
        self.assertTrue(self.__is_text_present("021"))

    # Test LogIn HelpDesk/Index/Services/Active Tickets
    def test15_helpdesk_solve_ticket(self):
        print ("Testing supervisor solve ticket ... ")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/home/login/")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys('gigi.h')
        password_input = driver.find_element_by_name("password")
        password_input.send_keys('hgigtest123')
        driver.find_element_by_name('Submit').click()
        # Asserting True index page text
        self.assertTrue(self.__is_text_present("simpleTicket is a new self-service app that uses"))
        driver.find_element_by_name('services').click()
        # Asserting True Services page text information
        self.assertTrue(self.__is_text_present("View contact info for all employees"))
        driver.find_element_by_name('solve_tickets').click()
        # Asserting True active tickets page text information
        self.assertTrue(self.__is_text_present("All Active Tickets"))
        self.assertTrue(self.__is_text_present("Cristina George"))
        self.assertTrue(self.__is_text_present("Office License"))
        self.assertTrue(self.__is_text_present("MS 2010 Office license has expired."))
        self.assertTrue(self.__is_text_present("Ok"))
        self.assertTrue(self.__is_text_present("Medium"))
        self.assertTrue(self.__is_text_present("Approved"))
        # Opening active ticket
        driver.find_element_by_name(str(self.id_ticket)).click()
        self.assertTrue(self.__is_text_present("Ticket Information"))
        self.assertTrue(self.__is_text_present("Cristina George"))
        self.assertTrue(self.__is_text_present("Office License"))
        self.assertTrue(self.__is_text_present("Processing"))
        # Approving Ticket
        status_select = Select(driver.find_element_by_id('status'))
        status_select.select_by_visible_text('Closed')
        title_comments = driver.find_element_by_name("comments")
        title_comments.send_keys('Solved')
        driver.find_element_by_name('submit').click()
        # Asserting True confirmation message
        self.assertTrue(self.__is_text_present("You have successfully updated the ticket status!"))
        # Asseting that the previous approve ticket is now removed from list
        driver.get("http://127.0.0.1:8000/helpd/active_tickets/")
        self.assertFalse(self.__is_text_present("Office License"))
        self.assertFalse(self.__is_text_present("MS 2010 Office license has expired."))

    # Test LogIn HelpDesk/Index/Services/Closed Tickets
    def test16_helpdesk_solved_tickets(self):
        print ("Testing supervisor solved tickets ... ")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/home/login/")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys('gigi.h')
        password_input = driver.find_element_by_name("password")
        password_input.send_keys('hgigtest123')
        driver.find_element_by_name('Submit').click()
        # Asserting True index page text
        self.assertTrue(self.__is_text_present("simpleTicket is a new self-service app that uses"))
        driver.find_element_by_name('services').click()
        # Asserting True Services page text information
        self.assertTrue(self.__is_text_present("View contact info for all employees"))
        driver.find_element_by_name('closed_tickets').click()
        # Asserting True closed tickets page text information
        self.assertTrue(self.__is_text_present("All Closed Tickets"))
        self.assertTrue(self.__is_text_present("Cristina George"))
        self.assertTrue(self.__is_text_present("Office License"))
        self.assertTrue(self.__is_text_present("MS 2010 Office license has expired."))
        self.assertTrue(self.__is_text_present("Solved"))
        self.assertTrue(self.__is_text_present("Medium"))

    # Test LogIn HelpDesk/Index/Services/Active Orders
    def test17_helpdesk_solve_order(self):
        print ("Testing supervisor solve order ... ")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/home/login/")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys('gigi.h')
        password_input = driver.find_element_by_name("password")
        password_input.send_keys('hgigtest123')
        driver.find_element_by_name('Submit').click()
        # Asserting True index page text
        self.assertTrue(self.__is_text_present("simpleTicket is a new self-service app that uses"))
        driver.find_element_by_name('services').click()
        # Asserting True Services page text information
        self.assertTrue(self.__is_text_present("View contact info for all employees"))
        driver.find_element_by_name('solve_orders').click()
        # Asserting True active orders page text information
        self.assertTrue(self.__is_text_present("All Active Orders"))
        self.assertTrue(self.__is_text_present("Cristina George"))
        self.assertTrue(self.__is_text_present("Desk Lamp"))
        self.assertTrue(self.__is_text_present("Improve office lighting"))
        self.assertTrue(self.__is_text_present("Ok"))
        self.assertTrue(self.__is_text_present("Medium"))
        self.assertTrue(self.__is_text_present("Approved"))
        # Opening active ticket
        driver.find_element_by_name(str(self.id_order)).click()
        self.assertTrue(self.__is_text_present("Order Information"))
        self.assertTrue(self.__is_text_present("Cristina George"))
        self.assertTrue(self.__is_text_present("Desk Lamp"))
        self.assertTrue(self.__is_text_present("Improve office lighting"))
        self.assertTrue(self.__is_text_present("Processing"))
        # Approving Ticket
        status_select = Select(driver.find_element_by_id('status'))
        status_select.select_by_visible_text('Closed')
        title_comments = driver.find_element_by_name("comments")
        title_comments.send_keys('Solved')
        driver.find_element_by_name('submit').click()
        # Asserting True confirmation message
        self.assertTrue(self.__is_text_present("You have successfully updated the order status!"))
        # Asseting that the previous approve ticket is now removed from list
        driver.get("http://127.0.0.1:8000/helpd/active_orders/")
        self.assertFalse(self.__is_text_present("Desk Lamp"))
        self.assertFalse(self.__is_text_present("Improve office lighting"))

    # Test LogIn HelpDesk/Index/Services/Closed Orders
    def test18_helpdesk_solved_orders(self):
        print ("Testing supervisor solved orders ... ")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/home/login/")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys('gigi.h')
        password_input = driver.find_element_by_name("password")
        password_input.send_keys('hgigtest123')
        driver.find_element_by_name('Submit').click()
        # Asserting True index page text
        self.assertTrue(self.__is_text_present("simpleTicket is a new self-service app that uses"))
        driver.find_element_by_name('services').click()
        # Asserting True Services page text information
        self.assertTrue(self.__is_text_present("View contact info for all employees"))
        driver.find_element_by_name('closed_orders').click()
        # Asserting True closed orders page text information
        self.assertTrue(self.__is_text_present("All Closed Orders"))
        self.assertTrue(self.__is_text_present("Cristina George"))
        self.assertTrue(self.__is_text_present("Desk Lamp"))
        self.assertTrue(self.__is_text_present("Improve office lighting"))
        self.assertTrue(self.__is_text_present("Solved"))
        self.assertTrue(self.__is_text_present("Medium"))