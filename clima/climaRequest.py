import requests

def getInfo(url = "https://dweet.io/get/latest/dweet/for/celula72"):

    response = requests.get(url)

    if(response.status_code == 200):
        content = list(response.json().get("with"))
        principales = content[0]
        return {}
    else:
        return "Error"
