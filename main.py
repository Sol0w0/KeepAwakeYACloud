import requests
import json
from time import sleep

instanceId = "<ИДЕНТИФИКАТОР МАШИНЫ>"
oAUTHtoken = "<ВАШ OAUTH ТОКЕН>"
    
def getIAMtoken():
    body = {"yandexPassportOauthToken":f"{oAUTHtoken}"}
    token = requests.post(url="https://iam.api.cloud.yandex.net/iam/v1/tokens",data=body)
    print("Токен получен")
    return json.loads(token.text)["iamToken"]

def pingServer(iamToken):
    header = {"Authorization":f"Bearer {iamToken}"}
    pingRes = requests.get(f"https://compute.api.cloud.yandex.net/compute/v1/instances/{instanceId}",headers=header)
    return json.loads(pingRes.text)["status"]
    
def disableIAMtoken(iamToken):
    header = {"Content-Type":"application/json","Authorization":f"Bearer {iamToken}"}
    body = {"iamToken":f"{iamToken}"}
    requests.post("https://iam.api.cloud.yandex.net/iam/v1/tokens:revoke",headers=header,data=body)
    print("Токен отозван")
       
def startServer(iamToken):
    header = {"Authorization":f"Bearer {iamToken}"}
    startup = requests.post(f"https://compute.api.cloud.yandex.net/compute/v1/instances/{instanceId}:start", headers=header)
    if startup.status_code == 200:
        print("Запущено")
  
def main():
    while True:
        sleep(600)
        iamToken = getIAMtoken()
        try:
            print("Шлю пинг...")
            if pingServer(iamToken) != "STOPPED":
                print("Сервер работает")
                raise Exception
            else:
                print("Сервер выключен")
                startServer(iamToken)
                raise Exception
        except:
            disableIAMtoken(iamToken)
    
if __name__ == "__main__":
    main()