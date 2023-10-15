import re
import requests
import json
from bs4 import BeautifulSoup
import urllib.parse

#-------------------------------------------------------------------------------------------------------------------------



def send_phone_number():
    
    num = str(input("please enter your phone number ? "))

    url = f"https://app.snapp.taxi/verify-cellphone-otp/?cellphone={num}&redirect_to=/https://app.snapp.taxi/login/?redirect_to=%2F"

    # num_char = []

    # for char in num:
    #     num_char.append(char)
    
    # if num_char[0] == "0":
    #     num_char[0] = '+98'

    # num = ''.join(num_char)
    
    # num = '{"cellphone":"+989936223354"}'

    # json_data  = json.loads(num)

    # req = requests.post(url,json={
    #     'cellphone': '+989936223354'
    # })
    
    # print(req)

    req = requests.get(url.text)

    print(req)




send_phone_number()

print