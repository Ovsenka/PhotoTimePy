from vk_api import vk_api
from dataclasses_ import ServerData, AccountData
from requests import post
import os
from exceptions import UploadPhotoError

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
        self.__prev_photo_id = -1
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
        
    def clear_profile_photo(self, post_id: int) -> None:
        own_id = self.get_profile_info().id
        all_photos = self.__api.photos.get(owner_id=own_id, album_id="profile")
        for dict_photo in all_photos['items']:
            if dict_photo['post_id'] == post_id:
                photo_id = dict_photo['id']
                self.__api.photos.delete(owner_id=own_id, photo_id=photo_id)
                return
    
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
            return ServerData(res['server'], res['hash'], res['photo'])
        raise UploadPhotoError(f"POST <{response.status_code}>")

    def upload_profile_photo(self) -> None:
        data =  self.upload_photo_on_server()
        try:
            res = self.__api.photos.saveOwnerPhoto(server=str(data.server), hash=data.hash, photo=data.photo)
            print("[OK] Photo has uploaded!")
            if self.__prev_photo_id != -1:
                self.clear_profile_photo(self.__prev_photo_id)
            self.__prev_photo_id = res['post_id']
        except Exception as e:
            print("Exception: SaveOwnerPhoto Error,", e)
    
