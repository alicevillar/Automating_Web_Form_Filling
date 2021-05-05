from faker import Faker


fake = Faker()
#criando uma variavel e inicializando com um dic vazio
user_data = {}

person1 = fake.profile()

#colocando dentro do dicionário: a chave será email e o valor será o que está dentro do dic person1
user_data["email"] = person1['mail']

user_data["gender"] = person1['sex']

full_name = person1['name'].split(" ")

#dicionário terá a chave first_name, q recebe o index zero do full_name
user_data["first_name"] = full_name[0]
#dicionário terá a chave last_name, q recebe o index 1 do full_name
user_data["last_name"] = full_name[1]

user_data["password"] = fake.password()

birthdate = person1['birthdate']

user_data["day"] = str(birthdate.day)
user_data["month"] = str(birthdate.month)
user_data["year"] = str(birthdate.year)



user_data["company"] = person1['company']

full_address = fake.address().split("\n")
user_data["address1"] = full_address[0]
user_data["address2"] = full_address[1]


user_data["city"] = full_address[1].split(",")[0] #choosing index 1, which corresponds to the city and then split and choose the element in the position 0

#Function to open my file with "r", which is the parameter only to read
#file = open("states_abreviation.txt","r")
#print(file.read())

#line = file.readline().split("\t") #split quando tiver o tamanho de um tab (4 espaços)
#print(line[1].replace("\n",""))#substituir \n por espaço vazio
#agora vamos perquisar o estado

#strip tira os espaços no começo e no final / Fazer um split aonde tem espaço vazio e pegar o index 0
state =full_address[1].split(",")[1].strip().split(" ")[0]


state_name = ""
# Percorrendo o arquivo que está sendo aberto
with open("states_abreviation.txt") as file:
    for line in file:
        name = line.split("\t")[0]
        sigla = line.split("\t")[1].replace("\n","")

        if state == sigla:
            state_name=name

print(state_name)
user_data["state"] = state_name

user_data["postal_code"] = str(full_address[1].split(",")[1].strip().split(" ")[1])

user_data["add_additional_info"]="No additional information"

print(user_data)


