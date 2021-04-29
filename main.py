from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as eco
from selenium.webdriver.common.by import By
from faker import Faker


#automatizacao de preenchimento de formulario

#####################################
# Passo 1: Configurar o driver
#
####################################

PATH = "C://Drivers/chromedriver.exe"
driver=webdriver.Chrome(PATH)

#####################################
# Passo 2:
# Acessar a pagina usando get
# Referenciar caixa de pesquisa
####################################

driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")

search_input=driver.find_element_by_xpath('//*[@id="email_create"]')

# Using the method send_keys, which is aimed to write in the search box
search_input.send_keys("Jennifer@uol.com.br")

# Using usando method send_keys to press ENTER
search_input.send_keys(Keys.ENTER)

#PREENCHENDO RADIO BUTTON

# localiza elemento pelo id e clica, mas não funciona justamente pq o formulário carrega num tempo diferente da página. Então, quando mando clicar na página, o formulário ainda não tá carregado
#driver.find_element_by_id("id_gender2").click()

# Waiting one second for the web browser to open the page
#Fixando o tempo de 30 segundos até que o radio button esteja pronto
#det que o driver vai esperar 30 segundo. det q seja até que o elemento abra. Encontro o elemento usando a classe By e o método ID dessa classe
# O locator é o - By.ID,"id_gender2" - , que é o parâmetro do método presence_of_element_located.
# presence_of_element_located returns WebElement once it is located
# A classe By dá uma estratégia para definir o parâmetro locator (ID é uma das estratégias que a classe By oferece)

element_radio_gender=WebDriverWait(driver,30).until(eco.presence_of_element_located((By.ID,"id_gender2")))

#o elemento foi encontrado e foi salvo nessa variável, então eu clico nela
element_radio_gender.click()

#preenchendo o box first name
#como não preciso clicar enter nao preciso criar uma variável. Posso fazer a sintae toda junta :)
driver.find_element_by_xpath('//*[@id="customer_firstname"]').send_keys("Jennifer")

#preenchendo o box last name
driver.find_element_by_xpath('//*[@id="customer_lastname"]').send_keys("Jobs")

#preenchendo o box password
driver.find_element_by_xpath('//*[@id="passwd"]').send_keys("Ganesha!")

#preenchendo o box date of birth - box day (drop down)
select_day=Select(driver.find_element_by_id("days"))
# Selecting by value
select_day.select_by_value("4")

#preenchendo o box date of birth - box month (drop down)

select_month=Select(driver.find_element_by_id("months"))
select_month.select_by_value("1")

#preenchendo o box date of birth - box year (drop down)
select_year=Select(driver.find_element_by_id("years"))
select_year.select_by_value("1992")

#preenchendo check box
driver.find_element_by_id("newsletter").click()
driver.find_element_by_id("optin").click()






