from bs4 import BeautifulSoup
import requests


class Parser:
    html = ""                       # глобaльная переменная
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        news = self.html.find_all("div", class_="caption")
        for item in news:
            topic = item.find("li", class_="topic-info-blog").text
            cont = item.find("div", class_="topic-content text").text
            url = item.find("h3").find("a").get('href')
            exit_time = item.find("div", class_="topic-info small").find("li").text

            self.res.append({
                "topic": topic,
                "content": cont,
                "url": url,
                "time": exit_time
            })
        # print(self.res)

    #  Сохранение данных:

    def save(self):
        with open(self.path, "w") as f:            # self.path - Имя файла
            i = 1
            for item in self.res:
                f.write(f"NEW № {i}\n\nТЕМА: {item['topic']}\n\n"
                        f"СОДЕРЖАНИЕ: {item['content']}\nССЫЛКА: {item['url']}\n\n"
                        f"ВРЕМЯ ВЫХОДА: {item['time']}\n"
                        f"\n\n{'*' * 72}\n")
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()

#   ЗАПУСК - С ФАЙЛА 'run.py'

