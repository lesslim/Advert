import json
from advert import Advert


def test1():
    """
    Проверка на обращение через точку.
    """
    lesson_str = """{
        "title": "python",
        "price": 0,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
        }
    }"""

    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)

    assert lesson_ad.location.address == "город Москва, Лесная, 7"
    print("Pass test 1.")


def test2():
    """
    отсутствие title.
    """
    lesson_str = """{
        "price": 0,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
        }
    }"""

    lesson = json.loads(lesson_str)
    try:
        lesson_ad = Advert(lesson)
        print("FAILED TEST 2")
        print(lesson_ad)
    except ValueError:
        print("Pass test 2.")


def test3():
    """
    price < 0
    """
    lesson_str = """{
        "title": "python",
        "price": -3,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
        }
    }"""

    lesson = json.loads(lesson_str)
    try:
        lesson_ad = Advert(lesson)
        print("FAILED TEST 3")
        print(lesson_ad)
    except ValueError:
        print("Pass test 3.")


def test4():
    """
    invalid price
    """
    lesson_str = """{
        "title": "python",
        "price": "sgddf",
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
        }
    }"""

    lesson = json.loads(lesson_str)
    try:
        lesson_ad = Advert(lesson)
        print("FAILED TEST 4")
        print(lesson_ad)
    except ValueError:
        print("Pass test 4.")


def test5():
    """
    no price
    """
    lesson_str = """{"title": "python"}"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    assert lesson_ad.price == 0
    print("Pass test 5.")


def test6():
    """
    attribute is a keyword
    """
    lesson_str = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    assert lesson_ad.class_ == "dogs"
    print("Pass test 6.")


def test7():
    """
    Отображение жёлтого корги
    """
    lesson_str = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad)


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
