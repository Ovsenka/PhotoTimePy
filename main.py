import vk_api

session = vk_api.VkApi('+79869252329', 'Ovsenka200009')
session.auth()

vk = session.get_api()

