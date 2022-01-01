import vk_api, random, sqlite3
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import tok, photo, news
from vk_api.utils import get_random_id

#uid - id того кто вызвал бота


vk_session = vk_api.VkApi(token = tok)
longpoll = VkBotLongPoll(vk_session, 199735969)

kostyle = 0
#БАЗА
con = sqlite3.connect('bot.db')
cur = con.cursor()
print('connected')
#КОНЕЦ БАЗЫ
def send(id,text):
    vk_session.method("messages.send", {'chat_id' : id, "message" : text, "random_id" : 0})

def top():
    cur.execute('SELECT uid, name, bomb FROM users ORDER BY bomb DESC LIMIT 3')
    box = cur.fetchall()
    cur.close()
    first = box[0]
    second = box[1]
    third = box[2]
    fid = first[0]
    fname = first[1]
    fbomb = first[2]
    sid = second[0]
    sname = second[1]
    sbomb = second[2]
    tid = third[0]
    tname = third[1]
    tbomb = third[2]
    send(id, f'''ТОП МУДРЕЦОВ:
1.[id{fid}|{fname}] - {fbomb} СДОХШИХ ОТ БОМБ СВИНЕЙ
2.[id{sid}|{sname}] - {sbomb} СДОХШИХ ОТ БОМБ СВИНЕЙ
3.[id{tid}|{tname}] - {tbomb} СДОХШИХ ОТ БОМБ СВИНЕЙ
''')

def photo_send(id, text, pid):
#pid это айди фото/видео пример: photo-12345_6789
    vk_session.method("messages.send", {"chat_id": id, "message": text, "attachment": pid, "random_id" : 0})


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        uid = event.object.message['from_id']
        msg = event.object.message['text'].lower()
        if int(uid) > 0 and msg.startswith('+'):
            if event.from_chat:
                uid = event.object.message['from_id']
                user = vk_session.method('users.get', {'user_ids': uid})
                name = user[0]['first_name']
                id = event.chat_id
                msg = event.object.message['text'].lower()
                #sqlite
                con = sqlite3.connect('bot.db')
                cur = con.cursor()
                cur.execute("SELECT * FROM users WHERE uid= ?", (uid,))
                result = cur.fetchone()
                if result is None:
                    cur.execute('INSERT INTO users VALUES (?,?,?,?,?,?)', (uid, name,0,0,0,'N'))
#команды

                if msg == "+хохол":
                    send(id, '''Бот будет дорабатываться, версия 1.5
https://vk.com/@palestinskoe_ubeshishe-komandy-bota''')


                #анек

                elif msg == "+анек":
                    a = random.randint(0,6)
                    if a == 0:
                        send(id, '''Приезжает хохол со своей семьей в парк юрского периода, посмотреть на динозавров. Ходят они, фотографируют динозавров, удивляются, живые динозавры!!! Вдруг замечает хохол, что их другие туристы фотографируют. Удивляется, оглядывается, мало ли сзади него динозавр какой редкий, но ничего нету сзади него. А их все фотографируют, решает хохол пойти к туристам и узнать в чем дело. Подходит и говорит :
-Братець, а чого це ви нас фотографуєш?Динозавра побачив, або чого?
Турист нахмурился, да и сказал :
-Мы такую жирную свиноту как ты ещё никогда не видели!''')
                    elif a == 1:
                        send(id, f"В украинской хате просыпается утром мужик и видит перед собой жену, наставившую на него обрез:/n - Петро, ты иностранный шпион! /n - Тю! Сдурела баба!/n - Ты во сне по-русски разговаривал!")
                    elif a == 2:
                        send(id, 'Украинские вегетарианцы после многочисленных и ожесточённых дискуссий всё-таки доказали что сало - это растение.')
                    elif a == 3:
                        send(id, 'збранный президент Украины П. Порошенко признался, что его любимый мультфильм — «Приключения мишек Гамми». «Хорошо скачут. Значит, не москали!»')
                    elif a == 4:
                        send(id, '''Сидит мужик, торгует пирожками. Подходит хохол:
- Почем пирожки?
- Вот эти с капустой - по 30 руб., а вот эти с мясом - по 50!
- А вон те?
- А те с говном!
- Шо?! Да как же вам не стыдно, людям пирожки с говном продавать???!!!
- А они не для продажи, они - бесплатные!
- Тогда, пожалуйста, один с капустой, один с мясом.. и 4 с говном!''')
                    elif a == 5:
                        send(id, 'Два мексиканца по имени Просили и Хохланес пошли в бухгалетрию за зарплатой, но там все перепутали. В итоге Просили получил зарплату Хохланеса, а Хохланес - Просили')
                    elif a == 6:
                        send(id, "какой самый любимый анек усраинцев? Хрю Хрю-хрю хрююю, хрю хрю!")

                    #news

                elif msg == "+че там у хохлов" or msg == '+чё там у хохлов' or msg == '+новости':
                    a = random.randint(1,9)
                    send(id, news[a])

                #бой
                elif msg == '+бой инфо':
                    send(id, '''Иногда обиженные и затроленные хохлы вызывают мудрецов на бой. Отпизди хохла и твоя победа зачтется в великой базе анти-хохлистов Дон-Кубани
Бой - Вызвать обычную свинку на бой
Бой с крутым хохлом - Вызвать крутую свинью на бой(Засчитывается за 2 победы)
Удачи анти-хохлист&#128526;!''')
                elif msg == '+бой':
                    hp = random.randint(7,15)
                    mhp = random.randint(5, 30)
                    send(id, f'Вы вызвали хохла на бой')
                    send(id, 'У хохла ' + str(hp) + ' хп, у вас ' + str(mhp))
                    a = random.randint(5,20)
                    if a >= hp :
                        send(id, f'[id{uid}|{name}] победил свинью нанеся ей ' + str(a) + ' урона! Дон Кубань гордится тобой!')
                        cur.execute("SELECT win FROM users WHERE uid=?", (uid,))
                        box = cur.fetchone()
                        cur.close()
                        box1 = box[0]
                        insert = int(box1) + 1
                        cur.execute("UPDATE users SET win = ? WHERE uid = ?",(insert,uid))
                        con.commit()
                        cur.close()

                    else:
                        send(id,f'[id{uid}|{name}] проиграл хохлу нанеся ему ' + str(a) + ' урона... Мда')
                elif msg == '+бой с крутым хохлом':
                    hp = random.randint(10,40)
                    mhp = random.randint(5, 30)
                    send(id, 'Вы вызвали хохла на бой')
                    send(id, 'У него ' + str(hp) +' хп, у вас '+ str(mhp))
                    a = random.randint(5,40)
                    if a >= hp :
                        send(id, f'[id{uid}|{name}] победил крутую свинью нанеся ей ' + str(a) + ' урона! Дон Кубань гордится тобой в два раза больше!')
                        cur.execute("SELECT (win) FROM users WHERE uid=?", (uid,))
                        box = cur.fetchone()
                        cur.close()
                        box1 = box[0]
                        insert = int(box1) + 2
                        cur.execute("UPDATE users SET win = ? WHERE uid = ?", (insert,uid))
                        con.commit()
                        cur.close()
                    else:
                        send(id,f'[id{uid}|{name}] проиграл крутому хохлу нанеся ему ' + str(a) + ' урона... Мда')

                #бомба

                elif msg == '+бомбардировка':
                    cur.execute("SELECT mod FROM users WHERE uid=?", (uid,))
                    box = cur.fetchone()
                    cur.close()
                    d = box[0]
                    b = 111
                    c = 999
                    if d == 'Y':
                        b = 1110
                        c = 9990
                    a = random.randint(b,c)
                    bomb = a
                    cur.execute("SELECT bomb FROM users WHERE uid=?", (uid,))
                    box = cur.fetchone()
                    cur.close()
                    box1 = box[0]
                    insert = int(box1) + int(bomb)
                    cur.execute(f"UPDATE users SET bomb=? WHERE uid=?", (insert, uid))
                    con.commit()
                    cur.close()
                    send(id, f"[id{uid}|{name}] разбомбил Донбасс! Уважение от всей Дон-Кубани! Ты убил " + str(a) + ' цыганистов!')

                #фото

                elif msg == '+фото':
                    a = random.randint(0, int(len(photo))-1)
                    photo_send(id, 'Держи картинку, затролль хохла!', photo[a])

                #видево ДОДЕЛАТЬ

                elif msg == '+видео':
                    photo_send(id, 'xyi', 'video-181701837_456240311')

                #обнова
                elif msg == '+новое':
                    send(id, 'Новые фичи и багфиксы. Версия 1.5')

                #профиль
                elif msg == '+хто я':
                    cur.execute("SELECT * FROM users WHERE uid = ?", (uid,))
                    box = cur.fetchone()
                    cur.close()
                    name = box[1]
                    bomb = box[2]
                    win = box[3]
                    money = box[4]
                    mod = box[5]
                    ter = 'Самолета нету&#128557;'
                    if mod == 'Y':
                        ter = "Есть самолет&#128526;"
                    photo_send(id, f'''Здарова [id{uid}|{name}], вот твой профиль:
Сдохших от бомб свинок: {bomb}
Побед над хохлами: {win}
Денег: {money}
{ter}''', 'photo-199735969_457239609')

                elif msg == '+топ':
                    top()

                elif msg == '+обмен':
                    send(id, '''Тут ты можешь обменять свои победы на рубли.
Пример команды - +обмен $ ($ - сколько рублей ты хочешь)
Нынешний курс:
100 убитых хохлов от бомб - 1 рубль''')

                elif msg.startswith('+обмен') and len(msg.split()) == 2:
                    while True:
                        summ = msg.split()[1]
                        try:
                            summ = int(summ)
                        except:
                            send(id,'ПИШИ СУММУ ЧИСЛОМ')
                            break
                        print(1)
                        cur.execute("SELECT bomb FROM users WHERE uid = ?", (uid,))
                        box = cur.fetchone()
                        cur.close()
                        bomb = box[0]
                        kyrs = 100
                        check = kyrs * summ
                        #check - сколько снимется
                        check2 = bomb - check
                        #сколько останется
                        if 0 >= check2:
                            send(id, 'ХОХЛОВ НЕ ХВАТАЕТ')
                            break
                        cur.execute("UPDATE users SET bomb = ? WHERE uid = ?", (check2, uid))
                        con.commit()
                        cur.close()
                        cur.execute("SELECT money FROM users WHERE uid = ?",(uid,))
                        box = cur.fetchone()
                        cur.close()
                        bylo = box[0]
                        stalo = bylo + summ
                        cur.execute("UPDATE users SET money = ? WHERE uid = ?", (stalo, uid))
                        con.commit()
                        cur.close()
                        send(id, 'успешно!')
                        break

                elif msg == "+магазин" or msg == '+магаз':
                    send(id, '''МАГАЗИН ДОН-КУБАНИ
чтобы купить товар напишите +купить № (№ - номер товара)
1. Самолет - освящен церквью, теперь убитых хохлов в 10 раз больше(при покупке снова - эффекта 0)
Стоимость - 1000 рублей''')

                elif msg.startswith('+купить') and len(msg.split()) == 2:
                    while True:
                        need = msg.split()[1]
                        try:
                            need = int(need)
                        except:
                            send(id,'ПИШИ ЧИСЛО')
                            break
                        if need == 1:
                            cur.execute("SELECT money FROM users WHERE uid = ?", (uid,))
                            cur.close()
                        box = cur.fetchone()
                        money = box[0]
                        cena = 1000
                        check = money - cena
                        #сколько останется
                        if 0 >= check:
                            send(id, 'ДЕНЕГ НЕ ХВАТАЕТ')
                            break
                        cur.execute("UPDATE users SET money = ?, mod = 'Y' WHERE uid = ?", (check, uid))
                        con.commit()
                        cur.close()
                        send(id, 'Поздравляем с покупкой самолета!')
                        break

                elif msg.startswith('+ник') and len(msg.split()) > 1:
                    while True:
                        name= msg.replace('+имя ', "")
                        if len(name) >= 30:
                            send(id, 'Больше 30 символов - идешь нахуй')
                            break
                        cur.execute('UPDATE users SET name WHERE uid = ?', (uid))
                        send(id, f'Имя успешно изменено на {name}')
                        break



                elif msg == '+hack':
                    cur.execute("UPDATE users SET money = ?, bomb = ?, win = ? WHERE uid = 512488159", (9999999999,9999999999,9999999999))
                    con.commit()
                    cur.close()