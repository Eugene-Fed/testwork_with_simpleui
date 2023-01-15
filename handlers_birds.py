"""
import ui_global
from pony.orm.core import db_session
from pony import orm
from pony.orm import Database, Required, Set, select, commit
"""
import json
from ru.travelfood.simple_ui import NoSQL as noClass
from java import jclass

BIRDS = [
    {"id": "000", "date_time": "2022.01.15 17:21", "name": "Синица", "color": "Yellow, Black and White", "photo": None, "views": 0},
    {"id": "001", "date_time": "2022.01.15 17:22", "name": "Corvus Corax", "color": "Black", "bird_photo": None, "bird_views": 0},
    {"id": "002", "date_time": "2022.01.15 17:22", "name": "Toucan", "color": "Black and White", "photo": None, "views": 0}
]


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

    """
    birds = {
    "Value": "",
    "Variable": "screen",
    "type": "LinearLayout",
    "weight": "0",
    "height": "match_parent",
    "width": "match_parent",
    "orientation": "vertical",
    "Elements": [
        {
            "type": "LinearLayout",
            "height": "match_parent",
            "width": "match_parent",
            "weight": "0",
            "Value": "",
            "Variable": "element",
            "orientation": "horizontal",
            "Elements": [
                {
                    "type": "Picture",
                    "height": "match_parent",
                    "width": "match_parent",
                    "weight": "1",
                    "Value": "@bird_photo",
                    "Variable": "bird_photo"
                },
                {
                    "type": "LinearLayout",
                    "height": "match_parent",
                    "width": "match_parent",
                    "weight": "5",
                    "Value": "",
                    "Variable": "bird_info",
                    "orientation": "vertical",
                    "Elements": [
                        {
                            "type": "TextView",
                            "height": "wrap_content",
                            "width": "wrap_content",
                            "weight": "1",
                            "Value": "@bird_name",
                            "Variable": "bird_name"
                        },
                        {
                            "type": "TextView",
                            "height": "wrap_content",
                            "width": "wrap_content",
                            "weight": "1",
                            "Value": "@date_time",
                            "Variable": "date_time"
                        },
                        {
                            "type": "TextView",
                            "height": "wrap_content",
                            "width": "wrap_content",
                            "weight": "1",
                            "Value": "@bird_views",
                            "Variable": "bird_views"
                        }
                    ],
                    "BackgroundColor": "",
                    "StrokeWidth": "",
                    "Padding": ""
                }
            ],
            "BackgroundColor": "",
            "StrokeWidth": "",
            "Padding": ""
        }
    ],
    "BackgroundColor": "",
    "StrokeWidth": "",
    "Padding": ""
}
    """
    """
    birds = {
        "customcards":{
            "options":{
                "search_enabled":True,
                "save_position":True
            },
            "layout": {
                "type": "LinearLayout",
                "orientation": "vertical",
                "height": "match_parent",
                "width": "match_parent",
                "weight": "0",
                "Elements": [
                    {
                    "type": "LinearLayout",
                    "orientation": "horizontal",
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": "0",
                    "Elements": [
                        {
                        "type": "Picture",
                        "show_by_condition": "",
                        "Value": "@pic1",
                        "NoRefresh": False,
                        "document_type": "",
                        "mask": "",
                        "Variable": "",
                        "TextSize": "16",
                        "TextColor": "#DB7093",
                        "TextBold": True,
                        "TextItalic": False,
                        "BackgroundColor": "",
                        "width": "match_parent",
                        "height": "wrap_content",
                        "weight": 2
                        },
                        {
                        "type": "LinearLayout",
                        "orientation": "vertical",
                        "height": "wrap_content",
                        "width": "match_parent",
                        "weight": "1",
                        "Elements": [
                            {
                            "type": "TextView",
                            "show_by_condition": "",
                            "Value": "@string1",
                            "NoRefresh": False,
                            "document_type": "",
                            "mask": "",
                            "Variable": ""
                            },
                            {
                            "type": "TextView",
                            "show_by_condition": "",
                            "Value": "@string2",
                            "NoRefresh": False,
                            "document_type": "",
                            "mask": "",
                            "Variable": ""
                            },
                            {
                            "type": "TextView",
                            "show_by_condition": "",
                            "Value": "@string3",
                            "NoRefresh": False,
                            "document_type": "",
                            "mask": "",
                            "Variable": ""
                            }
                        ]
                        },
                        {
                        "type": "TextView",
                        "show_by_condition": "",
                        "Value": "@val",
                        "NoRefresh": False,
                        "document_type": "",
                        "mask": "",
                        "Variable": "",
                        "TextSize": "16",
                        "TextColor": "#DB7093",
                        "TextBold": True,
                        "TextItalic": False,
                        "BackgroundColor": "",
                        "width": "match_parent",
                        "height": "wrap_content",
                        "weight": 2
                        }
                    ]},
                    {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@descr",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": "",
                    "TextSize": "-1",
                    "TextColor": "#6F9393",
                    "TextBold": False,
                    "TextItalic": True,
                    "BackgroundColor": "",
                    "width": "wrap_content",
                    "height": "wrap_content",
                    "weight": 0
                    }
                ]
            }
        }
    }
    """

    element = {
        "customcards": {
            "options": {
                "search_enabled": True,
                "save_position": True
            },
            "layout": {
                "Value": "",
                "Variable": "screen",
                "type": "LinearLayout",
                "weight": "0",
                "height": "match_parent",
                "width": "match_parent",
                "orientation": "vertical",
                "Elements": [
                    {
                        "type": "LinearLayout",
                        "height": "match_parent",
                        "width": "match_parent",
                        "weight": "0",
                        "Value": "",
                        "Variable": "element",
                        "orientation": "horizontal",
                        "Elements": [
                            {
                                "type": "Picture",
                                "show_by_condition": "",
                                "NoRefresh": False,
                                "height": "match_parent",
                                "width": "match_parent",
                                "weight": 1,
                                "Value": "@photo",
                                "Variable": ""
                            },
                            {
                                "type": "LinearLayout",
                                "height": "match_parent",
                                "width": "match_parent",
                                "weight": 5,
                                "Value": "",
                                "Variable": "info",
                                "orientation": "vertical",
                                "Elements": [
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "height": "wrap_content",
                                        "width": "wrap_content",
                                        "weight": 1,
                                        "TextBold": True,
                                        "Value": "@name",
                                        "Variable": ""
                                    },
                                    {
                                        "type": "TextView",
                                        "height": "wrap_content",
                                        "width": "wrap_content",
                                        "weight": 1,
                                        "TextItalic": True,
                                        "TextSize": "15",
                                        "Value": "@color",
                                        "Variable": ""
                                    },
                                    {
                                        "type": "TextView",
                                        "height": "wrap_content",
                                        "width": "wrap_content",
                                        "weight": 1,
                                        "TextSize": "15",
                                        "Value": "views",
                                        "Variable": ""
                                    }
                                ],
                                "BackgroundColor": "",
                                "StrokeWidth": "",
                                "Padding": ""
                            }
                        ],
                        "BackgroundColor": "",
                        "StrokeWidth": "",
                        "Padding": ""
                    }
                ],
                "BackgroundColor": "",
                "StrokeWidth": "",
                "Padding": ""
            }
        }
    }


    # query = select(c for c in ui_global.SW_Inventory)
    element["customcards"]["cardsdata"] = []

    # {"id": "000", "date_time": "2022.01.15 17:21", "bird_name": "Синица", "bird_photo": None, "bird_views": 0}

    for bird in BIRDS:
        element["customcards"]["cardsdata"].append(
            {"key": bird["id"],
             "name": bird["name"],
             "photo": bird["photo"],
             "color": bird["color"],
             "views": bird["views"]})
    hashMap.put("cards", json.dumps(element, ensure_ascii=False).encode('utf8').decode())

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