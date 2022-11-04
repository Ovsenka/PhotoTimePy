"""_summary_
    Main for start
"""
import os
from time import sleep
from vk_api_service import Client
from dtime import get_time, create_img

def mainloop():
    pass

def main():
    client = Client(login=os.environ.get("LOGIN_AUTH"),
                    password=os.environ.get("PASSWORD_AUTH"))
    print(client.get_profile())
    
    while True:
        time = get_time()
        print(time.hour, time.minute, time.second)     
        if int(time.second) <= 2: 
            create_img(time)
            client.upload_profile_photo()
            sleep(58)
        sleep(1)
            
            
              

if __name__ == "__main__":
    main()
