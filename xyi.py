import vk_api

token = ���� ����� ������ �������� ��� ������� vkhost.github.io
user = ���� ���� ���� ���� �� ������ ��������� ��� �������
session = vk_api.VkApi(token = token)
vk=session.get_api()

def send(user,msg):
    vk.messages.send(user_id = user, message = msg, random_id = 0)

while True:
    send(user, "����� ��")
    sleep(30)
