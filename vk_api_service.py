from vk_api import vk_api
from dataclasses_ import ServerData, AccountData
from requests import post
import os
from exceptions import UploadPhotoError, SavePhotoError

class Client:
    """_summary_
        Class for getting Api methods and custom some of them
    """
    def __init__(self, login: str, password: str):
        self.__session = vk_api.VkApi(
            login=login,
            password=password
        )
        self.__session.auth()
        print("User logged.")
        self.__api= self.__session.get_api()
    
    def get_api(self) -> vk_api.VkApiMethod:
        """_summary_
            Is used for getting API methods to use origin vk_api methods
        Returns:
            vk_api.VkApiMethod: https://dev.vk.com/method
        """
        return self.__api  
    
    def get_profile(self) -> dict:
        return self.__api.account.getProfileInfo()

    def get_profile_info(self) -> AccountData:
        user_d = self.get_profile()
        return AccountData(id=str(user_d['id']), 
                           name=user_d['first_name'], 
                           lastname=user_d['last_name'])
        
    def get_upload_server(self) -> str:
        own_id = self.get_profile_info().id
        response = self.__api.photos.getOwnerPhotoUploadServer(owner_id=own_id)
        return response['upload_url']

    def upload_photo_on_server(self) -> ServerData:
        upload_url = self.get_upload_server()
        script_dir = os.path.dirname(__file__)
        rel_path = "Temp/time"
        abs_file_path = os.path.join(script_dir, rel_path)
        file = {
         'method': "POST",
         'file': ('time.jpeg', open(abs_file_path, 'rb')),
        }
        response = post(upload_url, files=file)
        if response.status_code == 200:
            res = response.json()
            print("[OK] Photo uploaded!")
            return ServerData(res['server'], res['hash'], res['photo'])
        raise UploadPhotoError(f"POST <{response.status_code}>")

    def upload_profile_photo(self) -> None:
        data =  self.upload_photo_on_server()
        try:
            print("[INFO] Saving photo...")
            self.__api.photos.saveOwnerPhoto(server=str(data.server), hash=data.hash, photo=data.photo)
            print("[OK] Photo has saved")
        except:
            print("Exception: SaveOwnerPhoto Error")
    
    def clear_albums(self) -> None:
        pass
