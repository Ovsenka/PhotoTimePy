"""_summary_
    Main for start
"""
import os
from vk_api_service import Client
from dtime import get_time, create_img

def main():
    client = Client(login=os.environ.get("LOGIN_AUTH"),
                    password=os.environ.get("PASSWORD_AUTH"))
    #print(client.get_profile())
    time = get_time()
    print("Time:")
    print(time.hour, time.minute, time.second)
    create_img(time)
    

if __name__ == "__main__":
    main()
