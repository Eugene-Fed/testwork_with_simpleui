"""
import ui_global
from pony.orm.core import db_session
from pony import orm
from pony.orm import Database, Required, Set, select, commit
"""
import json
from ru.travelfood.simple_ui import NoSQL as noClass
from java import jclass

TEXT_SIZE = 20
BIRDS = [
    {"id": "000", "date_time": "2022.01.15 17:21", "name": "Titmouse", "color": "Yellow, Black and White", "photo": None, "views": 0},
    {"id": "001", "date_time": "2022.01.15 17:22", "name": "Corvus Corax", "color": "Black", "photo": None, "views": 0},
    {"id": "002", "date_time": "2022.01.15 17:23", "name": "Cockatoo", "color": "White and Yellow", "photo": None, "views": 0},
    {"id": "003", "date_time": "2022.01.15 17:24", "name": "Toucan", "color": "Black and White", "photo": None, "views": 0}
]

BIRDS_JSON = {
    "cards": [
        {
            "key": BIRDS[0]["id"],
            "picture": BIRDS[0]["photo"],
            "description": "",
            "items": [
                {
                    "key": "name",
                    "value": BIRDS[0]["name"],
                    "size": "15"
                },
                {
                    "key": "color",
                    "value": BIRDS[0]["color"],
                    "size": "10"
                },
                {
                    "key": "views",
                    "value": BIRDS[0]["views"],
                    "size": "10"
                },
                {
                    "key": "date_time",
                    "value": BIRDS[0]["date_time"],
                    "size": "10"
                }
            ]
        },
        {
            "key": BIRDS[1]["id"],
            "picture": BIRDS[1]["photo"],
            "description": "",
            "items": [
                {
                    "key": "name",
                    "value": BIRDS[1]["name"],
                    "size": "15"
                },
                {
                    "key": "color",
                    "value": BIRDS[1]["color"],
                    "size": "10"
                },
                {
                    "key": "views",
                    "value": BIRDS[1]["views"],
                    "size": "10"
                },
                {
                    "key": "date_time",
                    "value": BIRDS[1]["date_time"],
                    "size": "10"
                }
            ]
        },
        {
            "key": BIRDS[2]["id"],
            "picture": BIRDS[2]["photo"],
            "description": "",
            "items": [
                {
                    "key": "name",
                    "value": BIRDS[2]["name"],
                    "size": "15"
                },
                {
                    "key": "color",
                    "value": BIRDS[2]["color"],
                    "size": "10"
                },
                {
                    "key": "views",
                    "value": BIRDS[2]["views"],
                    "size": "10"
                },
                {
                    "key": "date_time",
                    "value": BIRDS[2]["date_time"],
                    "size": "10"
                }
            ]
        }
    ]
}


def generate_cards(data: list) -> json:
    """
    Функция для генерации JSON взамен константы BIRDS_OLD
    :param data:
    :return:
    """
    for d in data:
        pass
    return None

def on_create(hashMap, _files=None, _data=None):
    if not hashMap.containsKey("a"):
        hashMap.put("a", "")

    return hashMap


def on_input(hashMap, _files=None, _data=None):
    if hashMap.get("listener") == "btn_res":
        hashMap.put("toast", str(int(hashMap.get("a")) - int(hashMap.get("b"))))

    return hashMap

"""
def init_on_start(hashMap, _files=None, _data=None):
    ui_global.init()
    return hashMap


def input_qty(hashMap, _files=None, _data=None):
    with db_session:
        p = ui_global.Record(barcode=hashMap.get('barcode'), name=hashMap.get('nom'), qty=int(hashMap.get('qty')))
        commit()

    hashMap.put("ShowScreen", "Сканирование штрихкода")
    hashMap.put("toast", "Добавлено")
    return hashMap
"""

def search_input(hashMap, _files=None, _data=None):
    """
    :param hashMap:
    :param _files:
    :param _data:
    :return:
    Представление данных в JSON формате для последующего вывода в таблице
    """
    ncl = noClass("test_new_nosql")
    bird_1 = {"date_time": "2022.01.15 17:21", "bird_name": "Синица", "bird_photo": None, "bird_views": 0}
    ncl.put("000", json.dumps(bird_1, ensure_ascii=False), True)

    bird_2 = {"date_time": "2022.01.15 17:22", "bird_name": "Corvus Corax", "bird_photo": None, "bird_views": 0}
    ncl.put("001", json.dumps(bird_2, ensure_ascii=False), True)

    bird_3 = {"date_time": "2022.01.15 17:22", "bird_name": "Тукан", "bird_photo": None, "bird_views": 0}
    ncl.put("002", json.dumps(bird_3, ensure_ascii=False), True)

    # Поиск без индекса
    # res = ncl.findJSON("name", "Дарья")
    # jres = json.loads(str(res).encode("utf-8"))

    # Поиск по индексу
    res = ncl.findJSON_index("surnameindx", "surname", "Синицын")
    jres = json.loads(str(res).encode("utf-8"))

    hashMap.put("toast", str(jres))
    return hashMap

def inventory_on_start(hashMap, _files=None, _data=None):
    """
    :param hashMap:
    :param _files:
    :param _data:
    :return:
    Задаем стартовый набор данных о птицах в формате `кастомного` списка
    """

    table_graphic = {
        "type": "table",
        "textsize": TEXT_SIZE,
        "hidecaption": "true",
        "hideinterline": "true",
        "columns": [
            {
                "name": "id",
                "header": "ID",
                "weight": "2"
            },
            {
                "name": "name",
                "header": "Имя",
                "weight": "5"
            }
        ],
        "rows": []
    }
    table_new = {
        "customcards": {
            "options": {
                "search_enabled": True,
                "save_position": True
            },
            "layout": {
                "type": "LinearLayout",
                "orientation": "vertical",
                "weight": "0",
                "height": "match_parent",
                "width": "match_parent",
                "Elements": [
                    {
                        "type": "LinearLayout",
                        "height": "wrap_content",
                        "width": "match_parent",
                        "weight": "0",
                        "orientation": "horizontal",
                        "Elements": [
                            {
                                "type": "Picture",
                                "show_by_condition": "",
                                "NoRefresh": False,
                                "height": "wrap_content",
                                "width": "match_parent",
                                "weight": 1,
                                "Value": "@photo",
                                "Variable": ""
                            },
                            {
                                "type": "LinearLayout",
                                "height": "wrap_content",
                                "width": "match_parent",
                                "weight": 5,
                                "orientation": "vertical",
                                "Elements": [
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "NoRefresh": False,
                                        "weight": 1,
                                        "TextBold": True,
                                        "Value": "@name"
                                    },
                                    {
                                        "type": "TextView",
                                        "NoRefresh": False,
                                        "weight": 1,
                                        "TextItalic": True,
                                        "TextSize": "15",
                                        "Value": "@color"
                                    },
                                    {
                                        "type": "TextView",
                                        "NoRefresh": False,
                                        "weight": 1,
                                        "TextSize": "15",
                                        "Value": "@views",
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            "cardsdata": []
        }
    }

    # table_new["customcards"]["cardsdata"] = []
    # {"id": "002", "date_time": "2022.01.15 17:22", "name": "Toucan", "color": "Black and White", "photo": None, "views": 0}
    for bird in BIRDS:
        table_graphic['rows'].append({"id": str(bird["id"]), "name": str(bird["name"])})
        table_new["customcards"]["cardsdata"].append(
            {"key": str(bird["id"]),
             "name": str(bird["name"]),
             "photo": str(bird["photo"]),
             "color": str(bird["color"]),
             "views": str(bird["views"])
             })

    # print(json.dumps(table_old["rows"], ensure_ascii=False))
    hashMap.put("table_graphic", json.dumps(table_graphic))
    # hashMap.put("table_old", json.dumps(table_new, ensure_ascii=False))
    hashMap.put("cards", json.dumps(table_new, ensure_ascii=False))
    return hashMap


def putget_input(hashMap, _files=None, _data=None):
    """
    :param hashMap:
    :param _files:
    :param _data:
    :return:
    Управляющая функция для кнопок в изначальном примере интерфейса для добавления записей в базу
    """
    noClass = jclass("ru.travelfood.simple_ui.NoSQL")
    ncl = noClass("test_new_nosql")

    if hashMap.get("listener") == "btn_text":
        ncl.put("k1", "Это строка", True)
        res1 = ncl.get("k1")
        hashMap.put("toast", f"`{res1}`: тип {type(res1)}")

    if hashMap.get("listener") == "btn_number":
        ncl.put("k2", 555, True)
        res2 = ncl.get("k2")
        hashMap.put("toast", f"`{res2}`: тип {type(res2)}")

    if hashMap.get("listener") == "btn_boolean":
        ncl.put("k3", True, True)
        res3 = ncl.get("k3")
        hashMap.put("toast", f"`{res3}`: тип {type(res3)}")

    if hashMap.get("listener") == "btn_destroy":
        ncl.destroy()
        hashMap.put("speak", "Attention! All data has been destroyed!")

    if hashMap.get("listener") == "btn_destroy":
        ncl.destroy()
        hashMap.put("speak", "Attention! All data has been destroyed!")

    return hashMap


def putget_start(hashMap, _files=None, _data=None):
    """
    :param hashMap:
    :param _files:
    :param _data:
    :return:
    Описание самой таблицы для вывода на экран (в классическом формате)
    """
    noClass = jclass("ru.travelfood.simple_ui.NoSQL")
    ncl = noClass("test_new_nosql")

    results = {
        "type": "table",
        "textsize": "15",
        "hidecaption": "false",
        "hideinterline": "false",
        "columns": [
            {
                "name": "id",
                "header": "ID",
                "weight": "1"
            },
            {
                "name": "value",
                "header": "Данные",
                "weight": "4"
            }
        ],
        "rows": []
    }

    keys = ncl.getallkeys()
    hashMap.put("toast", str(keys))

    jkeys = json.loads(keys)
    for k in jkeys:
        results['rows'].append({"id": str(k), "value": str(ncl.get(k))})

    hashMap.put("table", json.dumps(results))
    return hashMap


def init(hashMap, _files=None, _data=None):
    ncl = noClass("test_new_nosql")
    ncl.run_index("surnameindx", "surname")

    return hashMap


if __name__ == "__main__":
    _ = inventory_on_start(hashMap=None)
