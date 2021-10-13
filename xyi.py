import vk_api

token = сюда токен своего аккаунта без ковычек vkhost.github.io
user = сюда пиши айди кого ты хочешь разъебать без ковычек
session = vk_api.VkApi(token = token)
vk=session.get_api()

def send(user,msg):
    vk.messages.send(user_id = user, message = msg, random_id = 0)

while True:
    send(user, "пизда те")
    sleep(30)
