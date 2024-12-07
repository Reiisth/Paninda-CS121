# Paninda: Sari-sari Store Inventory Management System
This project is a final requirement for CS121-Advance Computer Programming.

## I.	PROJECT OVERVIEW
### RATIONALE
Sari-sari stores are familiar businesses found in almost every community in the country. According to the Asian Preparedness Partnership, the Philippines’ small business sector is made up of 1.3 million sari-sari store businesses. Because of their prominence, the Philippine News Agency (2024) considers sari-sari stores as an important part of economic growth.
Sari-sari stores are typically considered as family business and depend on the family members for their administration. This familial scale of sari-sari stores opens them up to a vulnerability when it comes to inventory management. Families are typically busy and do not bother themselves to conduct proper inventory management because of its cumbersome nature.
This lack of inventory management systems often leads to shortages, surpluses, and even waste. When the store’s inventory is not subjected to regular tracking, products are often left to expire on the shelves, which gives way to different risks associated with food or products that have gone beyond their expiration. This situation is not only wasteful but also dangerous.

### SCOPE AND LIMITATIONS
Paninda is a project created to abridge this inventory process for tinderas across the country and make food and product waste a thing of the past. This project’s goal is to create an inventory system that is easy to understand and simple to use.
This system focuses on having an automated inventory system where expired and low quantity products are sorted automatically and are easy to identify. But this system does not handle store sales, orders, or transactions. Paninda caters to the not-so-tech-savvy store owners who does not have an inventory system in place for their business.

### GOALS AND TARGETS
Paninda has a main goal of reducing food and product waste by providing an inventory system that uses a database approach for sari-sari stores. More specifically it aims to fully replace pen and paper inventory with a digital application. Additionally, because of the database approach and automation, it aims to reduce food and product waste produced by sari-sari stores by 70% within the first year of implementation. 
Business-wise, Paninda’s target is to provide up to 30% more profit for the store owners by ensuring that products are fully stocked and fresh for sale. This goal should be achievable by store owners who implement Paninda within the first 6 months.

## II.	PYTHON CONCEPTS AND LIBRARIES
### Python Tkinter
Python Tkinter is a graphical user interface library available in Python that provides access to widgets such as labels, buttons, and frames. In this program, the Tkinter library was used mainly for GUI applications such as creating labels and frames. The tkk module within the Python Tkinter library was also utilized in parts of the system. Particularly within the database display with the use of the Treeview widgets.

### CustomTkinter
CustomTkinter is a UI-library based on Tkinter that offers more modern and customizable widgets. CustomTkinter was used in the majority of the GUI designs and elements of the program because of its modern and cleaner look. The library’s widgets offers a plethora of customizable attributes that allow the program to be truly unique. On top of that, the widgets are compatible with the default Tkinter elements.

### MySQL
In order to handle MySQL queries and connections, the program used the mysql.connector library. The collection of modules includes connection methods, query methods, and more complex database management methods for the Python program to make use of. The MySQL library was an essential part of this program.

## III.	SUSTAINABLE DEVELOPMENT GOALS
Paninda was a response or rather a simple aid to a problem of food and product waste along with profit loss within sari-sari stores in the Philippines. In the grand scheme of things, Paninda is a building block to achieve a United Nations Sustainable Development Goal. Specifically, this project aligns the most with SDG No.12, Responsible Consumption and Production as well as SDG No.8, Decent Work and Economic Growth. 
Paninda’s main goal is to reduce the waste that sari-sari stores produce by ensuring that the inventory of the store is up to date and is constantly in check of potential waste in both stocks and in profit. The first part of this mission is clearly in line with the goal of responsible consumption and production as Paninda helps with managing products and ensuring their quality for everyone.
Additionally, an aim for Paninda is to maximize profit for sari-sari stores by having a system in place for tracking products that are out of stock or not selling well. This allows sari-sari store owners to make informed decisions and make improvements to their business. This additional functionality generates a more economical business model that can work for every sari-sari store in the country.

## IV.	PROGRAM/SYSTEM INSTRUCTIONS

The program requires some initial setup for it to work without errors. To set-up the program, follow these instructions:

**1. Import and start the premade database**
   - Navigate to the program files and open the _‘database’_ folder
   - Select the _‘paninda_db’_ file and import it with the help of PHPmyAdmin
   - Once completed, start the MySQL database in your XAMPP Control Panel
**2. Download all the system fonts**
     - Go to the _‘fonts’_ folder in the program files
     - Select all the font files
     - Right click and choose to install
**3. Start the program**

  a. Open the ‘main.py’ in with the help of any IDE
  b. Run it

***IMPORTANT NOTES:***
Within the Paninda Database, there are existing data used for demonstrating the functionality of the software. Use this information when logging into the system to access the demo data:
**USERNAME:**_ admin_
**PASSWORD:**_ jasjas_

