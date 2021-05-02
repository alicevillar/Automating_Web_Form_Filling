from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as eco
from selenium.webdriver.common.by import By
from faker import Faker


################################################################
#   Part 1. INITIALIZING
#   1.1. Configuring the driver
#   1.2. Accessing the webpage using method get usando get
#   1.3. Referencing search box
#   1.4. Writing in the search box
#   1.5. Using method send_keys to press ENTER
#   1.6. Give some time for web browser to open the page
###############################################################

# Part 1.1 Configuring the driver
PATH = "C://Drivers/chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Part 1.2. Accessing the webpage using method get usando get
driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")

# Part 1.3. Referencing search box
search_input = driver.find_element_by_xpath('//*[@id="email_create"]')

# Part 1.4. Using the method send_keys, which is aimed to write in the search box
search_input.send_keys("Jennifer@uol.com.br")

# Part 1.5. Using method send_keys to press ENTER
search_input.send_keys(Keys.ENTER)

# Part 1.6. Give some time for web browser to open the page
element_radio_gender = WebDriverWait(driver, 30).until(eco.presence_of_element_located((By.ID, "id_gender2")))
# Found element is in this variable, so I'll click
element_radio_gender.click()

################################################################
#   Part 2. FORM FILLING ==> YOUR PERSONAL INFORMATION
#   2.1. Box - first name
#   2.2. Box - last name
#   2.3. Box - password
#   2.4. Box - date of birth (drop down)
#   2.5. Box - check box
###############################################################


# Part 2.1. Box - first name
driver.find_element_by_xpath('//*[@id="customer_firstname"]').send_keys("Jennifer")
# Here I don't need to click enter, so there is no need to create a variable. Thus, the syntaxe can be in one  line.

# Part 2.2. Box - last name
driver.find_element_by_xpath('//*[@id="customer_lastname"]').send_keys("Jobs")

# Part 2.3. Box - password
driver.find_element_by_xpath('//*[@id="passwd"]').send_keys("Ganesha!")

# Part 2.4. Box - date of birth (drop down)

# => Day
select_day = Select(driver.find_element_by_id("days"))
# Selecting by value
select_day.select_by_value("4")

# => Month
select_month = Select(driver.find_element_by_id("months"))
select_month.select_by_value("1")

# => Year
select_year = Select(driver.find_element_by_id("years"))
select_year.select_by_value("1992")

# Part 2.5. Box - check box
driver.find_element_by_id("newsletter").click()
driver.find_element_by_id("optin").click()


################################################################
#   Part 3. FORM FILLING ==>YOUR ADDRESS
#   3.1. Box - First name
#   3.2. Box - Last name
#   3.3. Box - Company
#   3.4. Box - Address
#   3.5. Box - Address 2
#   3.6. Box - City
#   3.7. Box - State
#   3.8. Box - Zip/Postal Code
#   3.9. Box - Country
#   3.10. Box - Additional information
#   3.11. Box - Home Phone
#   3.12. Box - Mobile Phone
#   3.13. Box - Assign an address alias for future reference
#   3.14. Box - Register: Using method send_keys to press ENTER
#
###############################################################


# Part 3.1. First name
driver.find_element_by_xpath('//*[@id="firstname"]')

# Part 3.2. Box - Last name
driver.find_element_by_xpath('//*[@id="lastname"]')

# Part 3.3. Box - Company
driver.find_element_by_xpath('//*[@id="company"]').send_keys("If Boutique Inc")

# Part 3.4. Box - Address
driver.find_element_by_xpath('//*[@id="address1"]').send_keys("T94 Grand St.")

# Part 3.5. Box - Address 2
driver.find_element_by_xpath('//*[@id="address2"]').send_keys("NY 10013")

# Part 3.6. Box - City
driver.find_element_by_xpath('//*[@id="city"]').send_keys("New York")

# Part 3.7. Box - State

select_year = Select(driver.find_element_by_id("id_state"))
select_year.select_by_value("32")

# Part 3.8. Box - Zip/Postal Code
driver.find_element_by_xpath('//*[@id="postcode"]').send_keys("64646")

# Part 3.9. Box - Country
select_year = Select(driver.find_element_by_id("id_country"))
select_year.select_by_value("21")

# Part 3.10. Box - Additional information
driver.find_element_by_xpath('//*[@id="other"]').send_keys("No additional information")

# Part 3.11. Box - Home Phone
driver.find_element_by_xpath('//*[@id="phone"]').send_keys("33445566")

# Part 3.12. Box - Mobile Phone
driver.find_element_by_xpath('//*[@id="phone_mobile"]').send_keys("992828282")

# Part 3.13. Box - Assign an address alias for future reference
driver.find_element_by_xpath('//*[@id="alias"]').send_keys("170 Ludlow St")

# Part 3.14. Box - Assign an address alias for future reference

# Part 3.14. Box - Register: Using method send_keys to press ENTER
search_input = driver.find_element_by_xpath('//*[@id="submitAccount"]')
search_input.send_keys(Keys.ENTER)
