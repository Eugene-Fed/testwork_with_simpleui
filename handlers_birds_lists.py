import json
# from ru.travelfood.simple_ui import NoSQL as noClass
import random
from java import jclass
import time
import datetime
import base64
from pathlib import Path
from android.widget import Toast
from com.chaquo.python import Python

TEXT_SIZE = 20
DB_BIRDS = 'birds_nosql'
NO_SQL_MODULE = 'ru.travelfood.simple_ui.NoSQL'
IMAGE_PATH = 'images'

"""
# Вариант для проброса в БД. Пока не взлетело. Доделать
BIRDS = {
    "000": {"date_time": "2022.01.15 17:21", "name": "Titmouse", "color": "Yellow, Black and White", "photo": None, "views": 0},
    "001": {"date_time": "2022.01.15 17:22", "name": "Corvus Corax", "color": "Black", "photo": None, "views": 0},
    "002": {"date_time": "2022.01.15 17:23", "name": "Cockatoo", "color": "White and Yellow", "photo": None, "views": 0},
    "003": {"date_time": "2022.01.15 17:24", "name": "Toucan", "color": "Black and White", "photo": None, "views": 0},
    "004": {"date_time": "2022.01.16 05:54", "name": "Blackbird", "color": "Black", "photo": None, "views": 0},
}
"""
BIRDS = [
    {"id": 0, "date_time": "2023-01-15 16:24:43", "name": "Titmouse", "color": "Yellow, Black and White", "photo": False, "views": 0},
    {"id": 1, "date_time": "2022-01-15 17:22:23", "name": "Corvus Corax", "color": "Black", "photo": False, "views": 0},
    {"id": 2, "date_time": "2022-01-15 17:23:15", "name": "Cockatoo", "color": "White and Yellow", "photo": False, "views": 0},
    {"id": 3, "date_time": "2022-01-15 17:24:49", "name": "Toucan", "color": "Black and White", "photo": False, "views": 0},
    {"id": 4, "date_time": "2022-01-16 05:54:12", "name": "Blackbird", "color": "Black", "photo": False, "views": 0}
]
BIRDS_VAR = "birds"

def get_birds(hashMap, _files=None, _data=None):
    # Универсальный обработчик списка птиц, который при необходимости создает эту переменную, в случае ее отсутствия
    if not hashMap.containsKey(BIRDS_VAR):
        # если переменной еще не существует - мы ее создаем из константного списка
        birds = json.dumps(BIRDS, ensure_ascii=False).encode('utf8').decode()
        hashMap.put(BIRDS_VAR, birds)
        return hashMap, BIRDS
    else:
        # если переменная с птицами уже существует - мы возвращаем ее
        return hashMap, json.loads(hashMap.get(BIRDS_VAR))

def append_birds(hashMap, _files=None, _data=None):
    # Универсальный расширитель списка птиц. Забираем hashMap из get_birds(), чтобы он 100% уже существовал
    hashMap, birds = get_birds(hashMap)
    # birds = json.loads(str(get_birds(hashMap).get(BIRDS_VAR)).encode("utf-8"))
    birds.append(_data)   # не прокатило, ибо hashMap не сохраняет значения между Процессами
    BIRDS.append(_data)   # TODO - заменить этот говнокод. Он РАБОТАЕТ, но надо прокидывать даннные сразу в БД, а не менять константы
    hashMap.put(BIRDS_VAR, json.dumps(birds, ensure_ascii=False).encode('utf8').decode())
    return hashMap, birds

def create_bird_on_load(hashMap, _files=None, _data=None):
    # Обработчик загрузки экрана "Создать птицу"
    if not hashMap.containsKey("new_name"):
        hashMap.put("new_name","")
    if not hashMap.containsKey("new_color"):
        hashMap.put("new_color","")
    return hashMap

def create_bird_on_input(hashMap, _files=None, _data=None):
    # Обработчик ввода данных экрана "Создать птицу"
    if hashMap.get("listener") == "btn_create":
        _, birds = get_birds(hashMap)
        hashMap, _ = append_birds(hashMap, _data={
            "id": len(birds),
            "date_time": str(datetime.datetime.now()).split('.')[0],
            "name": hashMap.get("new_name"),
            "color": hashMap.get("new_color"),
            "photo": None,
            "views": 0
        })
        hashMap.put("toast", "ПТИЧКА СОЗДАНА")
        # hashMap.put("StartProcessHashMap", "Птицы")   # автоматически переходим на список птиц. но механика так себе, лучше без нее
    return hashMap

def customcards_on_load(hashMap, _files=None, _data=None):
    # Обработчик загрузки экрана "Список птиц"
    """
    noClass = jclass(NO_SQL_MODULE)
    ncl = noClass(DB_BIRDS)
    """
    # TODO - Выяснить как подключать дополнительные файлы к проекту и вынести этот шаблон в .json-файл
    birds_table = { "customcards": {
            "options":{
              "search_enabled":True,
              "save_position":False
            },
            "layout": {
                "type": "LinearLayout",
                "orientation": "horizontal",
                "height": "wrap_content",
                "width": "match_parent",
                "weight": "0",
                "Elements": [
                {
                    "type": "Picture",
                    "Value": "@photo",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": "photo",
                    "BackgroundColor": "#DB7093",
                    "width": "match_parent",
                    "height": "wrap_content",
                    "weight": 1
                },
                {
                    "type": "LinearLayout",
                    "orientation": "vertical",
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": 4,
                    "Elements": [
                    {
                        "type": "TextView",
                        "show_by_condition": "",
                        "Value": "@name",
                        "NoRefresh": False,
                        "document_type": "",
                        "mask": "",
                        "Variable": "",
                        "TextSize": "20",
                        "TextColor": "#DB7093",
                        "TextBold": True,
                        "TextItalic": False,
                        "BackgroundColor": "",
                        "width": "match_parent",
                        "height": "wrap_content",
                        "weight": 2
                    },
                    {
                        "type": "TextView",
                        "show_by_condition": "",
                        "Value": "@color",
                        "NoRefresh": False,
                        "document_type": "",
                        "mask": "",
                        "Variable": ""
                    },
                    {
                        "type": "TextView",
                        "show_by_condition": "",
                        "Value": "@views",
                        "NoRefresh": False,
                        "document_type": "",
                        "mask": "",
                        "Variable": ""
                    }
                    ]
                }
                ]
        },
        "cardsdata": []
    }
    }

    """
    # TODO - разобраться почему не взлетело 
    # json.loads(ncl.encode("utf-8"))
    for key in ncl.getallkeys():            # скорее всего поэтому. getallkeys возвращает вообще всё, а не только ID
        hashMap.put("toast", str(key))
        data = ncl.get(key)
        table_new["customcards"]["cardsdata"].append({
            "key": str(key),
            "name": str(data["name"]),
            "photo": str(data["photo"]),
            "color": str(data["color"]),
            "views": str(data["views"])
        })
    """
    hashMap, birds = get_birds(hashMap)
    # Первоначальный тестовый вариант с работой по списку вместо БД
    for bird in birds:
        if not bird["photo"]:           # Если фотография не задана - преобразовать с диска в Base64
            image_path = Path.joinpath(IMAGE_PATH, f'{bird["id"]}.jpg')
            with open(image_path, "rb") as image_file:
                image_base64 = base64.b64encode(image_file.read())

        birds_table["customcards"]["cardsdata"].append(
            {"key": str(bird["id"]),
             "name": str(bird["name"]),
             "photo": str(image_base64),
             "color": str(bird["color"]),
             "views": str(bird["views"])
             })

    if not hashMap.containsKey("cards"):
        hashMap.put("cards", json.dumps(birds_table, ensure_ascii=False).encode('utf8').decode())
    return hashMap


def customcards_on_touch(hashMap, _files=None, _data=None):
    # Обработчик интерфейса экрана "Список птиц"
    hashMap, birds = get_birds(hashMap)
    """
    noClass = jclass("ru.travelfood.simple_ui.NoSQL")
    ncl = noClass("birds_nosql")
    """
    if hashMap.get("listener") == "CardsClick":
        # запоминаем ID карты, чтобы передать в глобальные переменные необходимые значения
        selected_card_key = hashMap.get('selected_card_key')

        # TODO тут можно все красиво оформить через Pandas, но это надо еще модули подключать. Поэтому пока перебором.
        for bird in birds:
            if str(bird["id"]) == selected_card_key:
                for key in bird:
                    # передаем значения всех ключей из БД в одноименные глобальные переменные
                    hashMap.put(key, str(bird[key]))
        """
        # TODO - не разобрался с объектом БД от этой либы. Пока без нее
        # Находим запись в БД по ее идентификатору (он равен идентификатору карточки)
        selected_card = ncl.findJSON("id", selected_card_key)
        selected_card = json.loads(str(selected_card).encode("utf-8"))
        for key in selected_card:
            hashMap.put(key, selected_card[key])
        """
        hashMap.put("toast", str(selected_card_key))
        hashMap.put("ShowScreen", "Карточка")  # После того как данные для Детальной страницы получены, открываем ее
    """
    else:
        # card_data = json.loads(str(hashMap.get('card_data')))
        card_data = hashMap.get('card_data')  # оказалось сюда данные приходят только от кнопок, но не от карточек
        hashMap.put("toast", f"res={hashMap.get('listener')}/"
                             f"{str(hashMap.get('layout_listener'))}/"
                             f"{str(hashMap.get('card_data'))}")
    """
    return hashMap


def detail_card_on_load(hashMap, _files=None, _data=None):
    # Этот обработчик по сути лишний. Я не сразу понял почему Карточка перестала отображать данные.
    # Оказалось дело было не здесь. Эту функцию вообще можно убрать отсюда и из Редактора - все равно будет работать.
    if not hashMap.containsKey("photo"):
        hashMap.put("photo", None)
    else:
        hashMap.get("photo")
    if not hashMap.containsKey("name"):
        hashMap.put("name", "")
    else:
        hashMap.get("name")
    if not hashMap.containsKey("color"):
        hashMap.put("color", "")
    else:
        hashMap.get("color")
    if not hashMap.containsKey("views"):
        hashMap.put("views", "")
    else:
        hashMap.get("views")
    if not hashMap.containsKey("date_time"):
        hashMap.put("date_time", "")
    else:
        hashMap.get("date_time")
    return hashMap


def detail_card_touch(hashMap, _files=None, _data=None):
    # Обработчик кнопок экрана "Детальная страница"
    # Пока не использую, т.к. меню скрыл
    if hashMap.get("listener") == 'BACK_BUTTON':
        hashMap.put("ShowScreen", "Список")
    return hashMap


def init(hashMap, _files=None, _data=None):
    """
    noClass = jclass(NO_SQL_MODULE)
    ncl = noClass(DB_BIRDS)
    # TODO Для верности загоним данные в БД через цикл, хотя есть несколько методов для дампа. Разобраться потом.
    for key in BIRDS:
        # Пробрасываем ключи наших записей в качестве ключа базы
        ncl.put(key, json.dumps(BIRDS[key]), True)
    # ncl.run_index("id", key)  # В текущем не используем `быстрый` индекс, потому что не можем его задать заранее
    """
    hashMap, birds = get_birds(hashMap)
    return hashMap


if __name__ == '__main__':
    noClass = jclass(NO_SQL_MODULE)
    ncl = noClass(DB_BIRDS)
    customcards_on_load()
