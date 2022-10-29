from vk_api import vk_api


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

