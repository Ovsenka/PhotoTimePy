import vk_api

vk_session = vk_api.VkApi('+79869252329', 'Ovsenka200009')
vk_session.auth()

vk = vk_session.get_api()