from vk_api import vk_api
from dataclasses_ import ServerData, AccountData

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
            Is used for getting API methods to use non-custom vk_api methods
        Returns:
            vk_api.VkApiMethod: https://dev.vk.com/method
        """
        return self.__api  
    
    def get_profile(self) -> dict:
        return self.__api.account.getProfileInfo()

    def get_profile_info(self) -> AccountData:
        user_d = self.get_profile()
        return AccountData(id=user_d['id'], 
                           name=user_d['first_name'], 
                           lastname=user_d['last_name'])
        

    def upload_photo_on_server(self) -> ServerData:
        own_id = self.get_profile_info().id
        #self.__api.getOwnerPhotoUploadServer(owner_id=own_id)
        pass

    def upload_profile_photo(self) -> None:
        #response =  upload_photo_on_server() -> (server, hash, photo)
        # upload profile photo(server, hash, photo)
        pass
    
    def clear_albums(self) -> None:
        pass
