import json
import random
import time
import base64

TEXT_SIZE = 20
BIRDS = [
    {"id": "000", "date_time": "2022.01.15 17:21", "name": "Titmouse", "color": "Yellow, Black and White", "photo": None, "views": 0},
    {"id": "001", "date_time": "2022.01.15 17:22", "name": "Corvus Corax", "color": "Black", "photo": None, "views": 0},
    {"id": "002", "date_time": "2022.01.15 17:23", "name": "Cockatoo", "color": "White and Yellow", "photo": None, "views": 0},
    {"id": "003", "date_time": "2022.01.15 17:24", "name": "Toucan", "color": "Black and White", "photo": None, "views": 0}
]

def customcards_on_open(hashMap, _files=None, _data=None):
    table_new = { "customcards": {
            "options":{
              "search_enabled":True,
              "save_position":True
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
                    },
                    {
                        "type": "Button",
                        "show_by_condition": "",
                        "Value": "#f290",
                        "TextColor": "#DB7093",
                        "Variable": "btn_tst1",
                        "NoRefresh": False,
                        "document_type": "",
                        "mask": ""
                    }
                    ]
                }
                ]
        }

    }
    }
   
    table_new["customcards"]["cardsdata"]=[]


    for bird in BIRDS:
        # table_graphic['rows'].append({"id": str(bird["id"]), "name": str(bird["name"])})
        table_new["customcards"]["cardsdata"].append(
            {"key": str(bird["id"]),
             "name": str(bird["name"]),
             "photo": str(bird["photo"]),
             "color": str(bird["color"]),
             "views": str(bird["views"])
             })

    if not hashMap.containsKey("cards"):
      hashMap.put("cards",json.dumps(table_new,ensure_ascii=False).encode('utf8').decode())
    return hashMap


def customtable_on_open(hashMap, _files=None, _data=None):
    
    j = { "customtable":         {
       "options":{
              "search_enabled":False,
              "save_position":True
            },
            
            "layout":  {
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
         } ,
       
               {
                "type": "PopupMenuButton",
                "show_by_condition": "",
                "Value": "Удалить;Проверить",
                "NoRefresh": False,
                "document_type": "",
                "mask": "",
                "Variable": "menu_delete"
                
                }
        ]
       },
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
       },{
          "type": "LinearLayout",
          "orientation": "horizontal",
          "height": "wrap_content",
          "width": "match_parent",
          "weight": "1",
          "Elements": [{
                    "type": "Button",
                    "show_by_condition": "",
                    "Value": "TST1",
                    "Variable": "btn_tst1",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": ""
                    
                },
                {
                    "type": "Button",
                    "show_by_condition": "",
                    "Value": "TST2",
                    "Variable": "btn_tst2",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": ""
                    
                }]}
      ]
}

    }
    }
   
    j["customtable"]["tabledata"]=[]
    for i in range(0,50):
        c =  {
        "key": str(i),
        "descr": "Pos. "+str(i),
        "val": str(random.randint(10, 10000))+" руб.",
        "string1": "Материнская плата ASUS ROG MAXIMUS Z690 APEX",
        "string2": "Гнездо процессора LGA 1700",
        "string3": "Частотная спецификация памяти 4800 МГц"
      }
        j["customtable"]["tabledata"].append(c)

    hashMap.put("table",json.dumps(j,ensure_ascii=False).encode('utf8').decode())
    
    return hashMap


def detail_card_on_open(hashMap, _files=None, _data=None):

    return hashMap

def customcards_touch(hashMap, _files=None, _data=None):
    if hashMap.get("listener") == "CardsClick":
        # запоминаем ID карты, чтобы передать в глобальные переменные необходимые значения
        selected_card_key = hashMap.get('selected_card_key')
        hashMap.put("toast", str(selected_card_key))
        # TODO тут можно все красиво оформить через Pandas, но это надо еще модули подключать. Поэтому перебором.
        for bird in BIRDS:
            if bird["id"] == selected_card_key:
                for key in bird:
                    # передаем значения всех ключей из БД в одноименные глобальные переменные
                    hashMap.put(key, bird[key])
        hashMap.put("ShowScreen", "Карточка")
        # click = True          # не знаю что это дает
    else:
        # card_data = json.loads(str(hashMap.get('card_data')))
        card_data = hashMap.get('card_data')  # оказалось сюда данные приходят только от кнопок, но не от карточек
        hashMap.put("toast", f"res={hashMap.get('listener')}/"
                             f"{str(hashMap.get('layout_listener'))}/"
                             f"{str(hashMap.get('card_data'))}")
    return hashMap


def customtable_touch(hashMap, _files=None, _data=None):
  if hashMap.get("listener")=="CardsClick":
    #hashMap.put("ShowScreen","Результат")
    click=True
  else:  
    hashMap.put("toast","res="+str(hashMap.get("listener")+"/"+str(hashMap.get("layout_listener"))+"/"+str(hashMap.get("card_data"))))
  return hashMap  


def customtable_result_input(hashMap, _files=None, _data=None):
    hashMap.put("ShowScreen", "Кастомная таблица")
    return hashMap


def tests_openinig1(hashMap, _files=None, _data=None):
    hashMap.put("SetTitle","Тестовое название")
    hashMap.put("getJSONScreen","")
    return hashMap


def tests_input1(hashMap,_files=None,_data=None):
    hashMap.put("toast",hashMap.get("JSONScreen"))
    return hashMap
