## Description
--------------
The project contains a simple IT style ticketing system build using the Django framework. The application supports four types of users. The **simple user** can create a ticket or an order, can view the status of the open tickets/orders and can view a report of all closed tickets/orders and reopen them if something went wrong. The **supervisor** is a user that has other users as subordinates. In addition to the users capabilities, the supervisor can approve or disapprove the subordinates opened tickets/orders. The **help desk operator** has a different set of tools. He can view the contact data for all the employees, process and solve approved/reopened tickets/orders and can view a report of all closed tickets. The **administrator** has access to all CRUD functionalities involving the users and help desk operators accounts, including setting the hierarchical relations in the company. Every ticket and order passes through the same life cycle **created** by the user, **approved** by the supervisor, **processing** and **solved** by the helpdesk operator or **reopened** by the initial user.

## Setup
--------
#### Prerequisites
* Django (tested with v1.9)
* Python (tested with v2.7)
* MySQL (tested with v5.7)
* (optional) Selenium (tested with v.2.53)

#### Runing the application
* Create a MySQL local connection or get the connection data for a remote one. 
* Go to *simpleTicket/simpleTicket/settings.py* and edit the *DATABASE* section to match the connection data from the previous step. Note that the user can switch to another database provider since Django uses a very simple migration system. All the configuration required is located in the *DATABASE* area.
* Using a command prompt window go to *simpleTicket/* and type <code>python manage.py runserver</code>. Access the prompted address. 

#### Runing the Selenium test suites
* Install Selenium.
* Go to *simpleTicket/* and run the commands contained in the *simpleTicket/Docs/Tests.txt* file for a specific functional test.
