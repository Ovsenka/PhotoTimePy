import vk_api
from config import LOGIN, PASSWORD


class Session:
	def __init__(self): 	
            session = vk_api.VkApi(LOGIN, PASSWORD)
            session.auth()
            return session.get_api()

