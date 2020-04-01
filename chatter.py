import requests
import ssl
import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#get data from api for countries
url = "https://corona.lmao.ninja/countries"
url_response = requests.get(url, verify=ssl.CERT_NONE)
data = url_response.json()

train = []

for k, row in enumerate(data):
    train.append(row['country']) #question

    train.append('Total cases '+str(row['cases'])) #answer
    #train.append('Today Cases '+str(row['todayCases']))
    #train.append('Today Deaths '+str(row['todayDeaths']))


# Create a new chat bot named Charlie
chatbot = ChatBot('Corona')

trainer = ListTrainer(chatbot)

trainer.train(train)

while True:
    request = input('You :')
    reaponse = chatbot.get_response(request)
    res_data = reaponse.serialize() #to get output in json format
    print('Bot :',res_data)
