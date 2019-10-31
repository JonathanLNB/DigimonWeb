import requests
import random

def getInfo():
    url = "https://digimon-api.herokuapp.com/api/digimon"
    response = requests.get(url)

    if(response.status_code == 200):
        content = list(response.json())
        aleatorios = content[:] 
        random.shuffle(aleatorios)
        return {"digimons": content, "principales": aleatorios[:3]}
    else:
        return "Error"

 