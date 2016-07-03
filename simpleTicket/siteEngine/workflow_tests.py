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

class SiteEngineWorkflowTests(StaticLiveServerTestCase):

    # Ticket Values
    id_ticket = 30
    ticket_owner = "Cristina George"
    ticket_category = "Software Problem"
    ticket_title = 'Office License'
    ticket_description = 'MS 2010 Office license has expired.'
    ticket_priority = 'Medium Priority'

    # Order Values
    id_order = 21

    fixtures = ['user-data.json']

    # --- Set Up and Tear Down Methods ---
    # Set Up
    @classmethod
    def setUpClass(cls):
        super(SiteEngineWorkflowTests, cls).setUpClass()
        cls.driver = webdriver.Chrome()
        print ("Initialized Chrome Driver ... ")

    # Tear Down
    @classmethod
    def tearDownClass(cls):
        print (" ... Destroying Resources")
        #cls.driver.quit()
        super(SiteEngineWorkflowTests, cls).tearDownClass()

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

    # Pauses the thread for 3 seconds
    def small_sleep(self):
        time.sleep(6)

    # Pauses the thread for 5 seconds
    def medium_sleep(self):
        time.sleep(10)
    # Pauses the thread for 10 seconds
    def large_sleep(self):
        time.sleep(14)

    # --- Test methods

    def test1_ticket_workflow(self):
        # ==== USER ===

        # --- Login
        print ("Asserting User Login ... ")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/home/login/")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys('cristina.g')
        password_input = driver.find_element_by_name("password")
        password_input.send_keys('gcritest123')
        self.medium_sleep()
        driver.find_element_by_name('Submit').click()

        # --- Index
        print ("Asserting Index Page ... ")
        # Asserting True index page text
        self.assertTrue(self.__is_text_present("simpleTicket is a new self-service app that uses"))
        # Asserting False auth error message
        self.assertFalse(self.__is_text_present("Invalid Username or Password provided! Please try again!"))
        # Asserting True index page element
        self.assertTrue(self.__is_element_present("name", "our-services"))
        self.medium_sleep()

        # --- Services
        driver.find_element_by_name('services').click()
        print ("Asserting Services Page ... ")
        # Asserting True Services page text information
        self.assertTrue(self.__is_text_present("Create Ticket"))
        self.assertTrue(self.__is_text_present("Create a new Ticket"))
        self.assertTrue(self.__is_text_present("If you need any assistance while creating an IT Ticket or placing any kind of order please contact our HelpDesk team."))
        self.medium_sleep()

        # --- Create Ticket
        driver.find_element_by_name('create_ticket').click()
        print ("Asserting Create Ticket Page ...")
        # Asserting True Create Ticket page text information
        self.assertTrue(self.__is_text_present("Create a Ticket"))
        # Populating form inputs
        category_select = Select(driver.find_element_by_id('type'))
        category_select.select_by_visible_text(self.ticket_category)
        title_input = driver.find_element_by_name("title")
        title_input.send_keys(self.ticket_title)
        description_input = driver.find_element_by_name("description")
        description_input.send_keys(self.ticket_description)
        priority_select = Select(driver.find_element_by_id('priority'))
        priority_select.select_by_visible_text(self.ticket_priority)
        self.medium_sleep()
        driver.find_element_by_name('submit').click()
        # Asserting True confirmation message
        self.assertTrue(self.__is_text_present("Ticket successfully created! You will be contacted as soon as possible."))
        self.small_sleep()

        # --- Services
        driver.find_element_by_name('services').click()
        print ("Asserting Services Page ... ")
        self.small_sleep()

        # --- Active Tickets
        driver.find_element_by_name('active_tickets').click()
        print ("Asserting Active Tickets Page ... ")
        # Asserting True Open Tickets page text information
        self.assertTrue(self.__is_text_present("Active Tickets for Cristina George"))
        self.assertTrue(self.__is_text_present(self.ticket_title))
        self.assertTrue(self.__is_text_present(self.ticket_description))
        self.assertTrue(self.__is_text_present("Medium"))
        self.assertTrue(self.__is_text_present("Sent"))
        self.large_sleep()

        # --- Log Out
        print ("Asserting Log Out ... ")
        driver.find_element_by_name('logout').click()
        # Asserting True logout page text
        self.assertTrue(self.__is_text_present("You Have Successfully Logged out of simpleTicket!"))
        self.medium_sleep()

        # === SUPERVISOR ===

        # --- Login
        print ("Asserting Supervisor Login ... ")
        driver.get("http://127.0.0.1:8000/home/login/")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys('george.r')
        password_input = driver.find_element_by_name("password")
        password_input.send_keys('rgeotest123')
        self.small_sleep()
        driver.find_element_by_name('Submit').click()

        # --- Index
        print ("Asserting Index Page ... ")
        self.assertTrue(self.__is_text_present("simpleTicket is a new self-service app that uses"))
        self.small_sleep()

        # --- Services
        print ("Asserting Services Page ... ")
        driver.find_element_by_name('services').click()
        # Asserting True Services page text information
        self.assertTrue(self.__is_text_present("Manage staff members"))
        self.large_sleep()

        # --- View Subordinates
        print ("Asserting Subordinates Page ... ")
        driver.find_element_by_name('subalterns').click()
        # Asserting True subordinates page text information
        self.assertTrue(self.__is_text_present("Active subalterns for George Rus"))
        self.assertTrue(self.__is_text_present("Cristina George"))
        self.assertTrue(self.__is_text_present("cristina.george@ticket.com"))
        self.assertTrue(self.__is_text_present("770"))
        self.assertTrue(self.__is_text_present("PDOM-DS"))
        self.medium_sleep()

        # --- Services
        print ("Asserting Services Page ... ")
        driver.find_element_by_name('services').click()
        # Asserting True Services page text information
        self.assertTrue(self.__is_text_present("Manage staff members"))
        self.small_sleep()

        # --- Approve Ticket
        print ("Asserting Approve Ticket Page ... ")
        driver.find_element_by_name('approve_tickets').click()
        # Asserting True open tickets page text information
        self.assertTrue(self.__is_text_present("Tickets pending the approval of George Rus"))
        self.assertTrue(self.__is_text_present(self.ticket_owner))
        self.assertTrue(self.__is_text_present(self.ticket_title))
        self.assertTrue(self.__is_text_present(self.ticket_description))
        self.assertTrue(self.__is_text_present("Medium"))
        self.assertTrue(self.__is_text_present("Sent"))
        self.medium_sleep()

        # --- Approve
        print ("Asserting the Ticket Approval Page ... ")
        # Opening active ticket
        driver.find_element_by_name(str(self.id_ticket)).click()
        self.assertTrue(self.__is_text_present("Ticket Information"))
        self.assertTrue(self.__is_text_present(self.ticket_owner))
        self.assertTrue(self.__is_text_present(self.ticket_title))
        self.small_sleep()
        # Approving Ticket
        status_select = Select(driver.find_element_by_id('status'))
        status_select.select_by_visible_text('Approved')
        title_comments = driver.find_element_by_name("comments")
        title_comments.send_keys('Ok')
        self.small_sleep()
        driver.find_element_by_name('submit').click()
        # Asserting True confirmation message
        self.assertTrue(self.__is_text_present("You have successfully updated the ticket status!"))
        self.small_sleep()

        # --- Approve Tickets
        print ("Asserting Approve Ticket Page ... ")
        # Asseting that the previous approve ticket is now removed from list
        driver.get("http://127.0.0.1:8000/home/subalterns_tickets/")
        self.assertFalse(self.__is_text_present(self.ticket_title))
        self.assertFalse(self.__is_text_present(self.ticket_description))
        self.medium_sleep()

        # --- Log Out
        print ("Asserting Log Out ... ")
        driver.find_element_by_name('logout').click()
        # Asserting True logout page text
        self.assertTrue(self.__is_text_present("You Have Successfully Logged out of simpleTicket!"))
        self.medium_sleep()

        # === HELPDESK ===

        # --- Login
        print ("Asserting HelpDesk Login ... ")
        driver.get("http://127.0.0.1:8000/home/login/")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys('gigi.h')
        password_input = driver.find_element_by_name("password")
        password_input.send_keys('hgigtest123')
        self.small_sleep()
        driver.find_element_by_name('Submit').click()

        # --- Index
        print ("Asserting Index Page ... ")
        self.assertTrue(self.__is_text_present("simpleTicket is a new self-service app that uses"))
        self.small_sleep()

        # --- Services
        print ("Asserting Services Page ... ")
        driver.find_element_by_name('services').click()
        # Asserting True Services page text information
        self.assertTrue(self.__is_text_present("View contact info for all employees"))
        self.medium_sleep()

        # --- Open Tickets
        print ("Asserting Open Ticket Page ... ")
        driver.find_element_by_name('solve_tickets').click()
        # Asserting True active tickets page text information
        self.assertTrue(self.__is_text_present("All Active Tickets"))
        self.assertTrue(self.__is_text_present(self.ticket_owner))
        self.assertTrue(self.__is_text_present(self.ticket_title))
        self.assertTrue(self.__is_text_present(self.ticket_description))
        self.assertTrue(self.__is_text_present("Ok"))
        self.assertTrue(self.__is_text_present("Medium"))
        self.assertTrue(self.__is_text_present("Approved"))
        self.large_sleep()

        # --- Process Ticket
        print ("Asserting Process Ticket Page ... ")
        # Opening active ticket
        driver.find_element_by_name(str(self.id_ticket)).click()
        self.assertTrue(self.__is_text_present("Ticket Information"))
        self.assertTrue(self.__is_text_present(self.ticket_owner))
        self.assertTrue(self.__is_text_present(self.ticket_title))
        self.assertTrue(self.__is_text_present("Processing"))
        self.medium_sleep()
        # Approving Ticket
        status_select = Select(driver.find_element_by_id('status'))
        status_select.select_by_visible_text('Closed')
        title_comments = driver.find_element_by_name("comments")
        title_comments.send_keys('Solved')
        self.medium_sleep()
        driver.find_element_by_name('submit').click()
        # Asserting True confirmation message
        self.assertTrue(self.__is_text_present("You have successfully updated the ticket status!"))
        self.small_sleep()

        # --- Open Tickets
        print ("Asserting Open Tickets Page ... ")
        # Asserting that the previous approve ticket is now removed from list
        driver.get("http://127.0.0.1:8000/helpd/active_tickets/")
        self.assertFalse(self.__is_text_present(self.ticket_title))
        self.assertFalse(self.__is_text_present(self.ticket_description))
        self.small_sleep()

        # --- Services
        print ("Asserting Services Page ... ")
        driver.find_element_by_name('services').click()
        # Asserting True Services page text information
        self.assertTrue(self.__is_text_present("View contact info for all employees"))
        self.medium_sleep()

        # --- Closed Tickets
        print ("Asserting Closed Tickets Page ... ")
        driver.find_element_by_name('closed_tickets').click()
        # Asserting True closed tickets page text information
        self.assertTrue(self.__is_text_present("All Closed Tickets"))
        self.assertTrue(self.__is_text_present(self.ticket_owner))
        self.assertTrue(self.__is_text_present(self.ticket_title))
        self.assertTrue(self.__is_text_present(self.ticket_description))
        self.assertTrue(self.__is_text_present("Solved"))
        self.assertTrue(self.__is_text_present("Medium"))
        self.medium_sleep()

        # --- Log Out
        print ("Asserting Log Out ... ")
        driver.find_element_by_name('logout').click()
        # Asserting True logout page text
        self.assertTrue(self.__is_text_present("You Have Successfully Logged out of simpleTicket!"))
        self.small_sleep()

        # === USER ===

        # --- Login
        print ("Asserting User Login ... ")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/home/login/")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys('cristina.g')
        password_input = driver.find_element_by_name("password")
        password_input.send_keys('gcritest123')
        self.small_sleep()
        driver.find_element_by_name('Submit').click()

        # --- Index
        print ("Asserting Index Page ... ")
        # Asserting True index page text
        self.assertTrue(self.__is_text_present("simpleTicket is a new self-service app that uses"))
        # Asserting False auth error message
        self.assertFalse(self.__is_text_present("Invalid Username or Password provided! Please try again!"))
        # Asserting True index page element
        self.assertTrue(self.__is_element_present("name", "our-services"))
        self.small_sleep()

        # --- Services
        driver.find_element_by_name('services').click()
        print ("Asserting Services Page ... ")
        # Asserting True Services page text information
        self.assertTrue(self.__is_text_present("Create Ticket"))
        self.assertTrue(self.__is_text_present("Create a new Ticket"))
        self.assertTrue(self.__is_text_present("If you need any assistance while creating an IT Ticket or placing any kind of order please contact our HelpDesk team."))
        self.small_sleep()

        # --- Closed Tickets
        print ("Asserting Closed Tickets Page ... ")
        driver.find_element_by_name('closed_ticket').click()
        # Asserting True closed tickets page text information
        self.assertTrue(self.__is_text_present("Closed Tickets for Cristina George"))
        self.assertTrue(self.__is_text_present(self.ticket_title))
        self.assertTrue(self.__is_text_present(self.ticket_description))
        self.assertTrue(self.__is_text_present("Solved"))
        self.assertTrue(self.__is_text_present("Medium"))
        self.medium_sleep()

        print ("... Test suite ended")