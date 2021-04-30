from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as eco
from selenium.webdriver.common.by import By
from faker import Faker

# automatizacao de preenchimento de formulario

################################################################
# Part 1: Initializing
#   1.1 Configuring the driver
#   1.2 Accessing the webpage using method get usando get
#   1.3 Referencing search box
#   1.4. Filling all buttons
###############################################################

# Part 1.1 Configuring the driver
PATH = "C://Drivers/chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Part 1.2 Accessing the webpage using method get usando get
driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")

# Part 1.3 Referencing search box
search_input = driver.find_element_by_xpath('//*[@id="email_create"]')

# Using the method send_keys, which is aimed to write in the search box
search_input.send_keys("Jennifer@uol.com.br")

# Using usando method send_keys to press ENTER
search_input.send_keys(Keys.ENTER)

# Part 1.4 Configuring the driver

# Filling Radio Button

# First, give some time for web browser to open the page
element_radio_gender = WebDriverWait(driver, 30).until(eco.presence_of_element_located((By.ID, "id_gender2")))
# Found element is in this variable, so I'll click
element_radio_gender.click()

# Box - first name
# como não preciso clicar enter nao preciso criar uma variável. Posso fazer a sintae toda junta :)
driver.find_element_by_xpath('//*[@id="customer_firstname"]').send_keys("Jennifer")

# preenchendo o box last name
driver.find_element_by_xpath('//*[@id="customer_lastname"]').send_keys("Jobs")

# preenchendo o box password
driver.find_element_by_xpath('//*[@id="passwd"]').send_keys("Ganesha!")

# Box - date of birth (drop down)
select_day = Select(driver.find_element_by_id("days"))
# Selecting by value
select_day.select_by_value("4")

# preenchendo o box date of birth - box month (drop down)

select_month = Select(driver.find_element_by_id("months"))
select_month.select_by_value("1")

# Box - date of birth - box year (drop down)
select_year = Select(driver.find_element_by_id("years"))
select_year.select_by_value("1992")

# Check box
driver.find_element_by_id("newsletter").click()
driver.find_element_by_id("optin").click()

# preenchendo Adress
# box - first name
driver.find_element_by_xpath('//*[@id="firstname"]')

# box - last name
driver.find_element_by_xpath('//*[@id="lastname"]')

# box - company
driver.find_element_by_xpath('//*[@id="company"]').send_keys("If Boutique Inc")

# Box - Address *

# Tyger City Shopping Centre
driver.find_element_by_xpath('//*[@id="address1"]').send_keys("T94 Grand St.")

# Box - Address 2
driver.find_element_by_xpath('//*[@id="address2"]').send_keys("NY 10013")

# Box - City
driver.find_element_by_xpath('//*[@id="city"]').send_keys("New York")

# Box - State

select_year = Select(driver.find_element_by_id("id_state"))
select_year.select_by_value("32")

# Box - Zip/Postal Code
driver.find_element_by_xpath('//*[@id="postcode"]').send_keys("64646")

# Box - Country
select_year = Select(driver.find_element_by_id("id_country"))
select_year.select_by_value("21")

# Box - Additional information
driver.find_element_by_xpath('//*[@id="other"]').send_keys("No additional information")

# Box - Home Phone
driver.find_element_by_xpath('//*[@id="phone"]').send_keys("33445566")

# Box - Mobile Phone
driver.find_element_by_xpath('//*[@id="phone_mobile"]').send_keys("992828282")

# Box - Assign an address alias for future reference
driver.find_element_by_xpath('//*[@id="alias"]').send_keys("170 Ludlow St")

# Box - Assign an address alias for future reference

# Box - Register: Using method send_keys to press ENTER
search_input = driver.find_element_by_xpath('//*[@id="submitAccount"]')
search_input.send_keys(Keys.ENTER)
