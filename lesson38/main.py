import requests
import threading
import time


def request_to(url1, url2, url3):
    start = time.perf_counter()
    requests.get(url1)
    requests.get(url2)
    requests.get(url3)
    end = time.perf_counter() - start
    return end


def asinc_request_to(url1, url2, url3):
    thread1 = threading.Thread(target=requests.get, args=(url1, ))
    thread2 = threading.Thread(target=requests.get, args=(url2, ))
    thread3 = threading.Thread(target=requests.get, args=(url3, ))
    start = time.perf_counter()
    thread1.start()
    thread2.start()
    thread3.start()
    end = time.perf_counter() - start
    return end


print(request_to("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0",
           "https://yandex.ru/?utm_campaign=search_brand%7C71806805&utm_content=4840419365%7C12222990391&utm_medium=search&utm_source=yandex&utm_term=%D1%8F%D0%BD%D0%B4%D0%B5%D0%BA%D1%81&yclid=17115372746328506367",
           "https://www.google.ru/webhp?hl=ru&gws_rd=ssl"))

print(asinc_request_to("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0",
           "https://yandex.ru/?utm_campaign=search_brand%7C71806805&utm_content=4840419365%7C12222990391&utm_medium=search&utm_source=yandex&utm_term=%D1%8F%D0%BD%D0%B4%D0%B5%D0%BA%D1%81&yclid=17115372746328506367",
           "https://www.google.ru/webhp?hl=ru&gws_rd=ssl"))


def to_degree(num1, num2, num3):
    start = time.perf_counter()
    a = num1**55564
    b = num2**55564
    c = num3**55564
    end = time.perf_counter() - start
    return end


def asinc_to_degree(num1, num2, num3):

    def degree(num):
        a = num**55564
        return a

    thread1 = threading.Thread(target=degree, args=(num1, ))
    thread2 = threading.Thread(target=degree, args=(num2, ))
    thread3 = threading.Thread(target=degree, args=(num3, ))
    start = time.perf_counter()
    thread1.start()
    thread2.start()
    thread3.start()
    end = time.perf_counter() - start
    return end


print(to_degree(11, 12, 13))
print(asinc_to_degree(1, 2, 3))
