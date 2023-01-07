from bs4 import BeautifulSoup
import requests

import csv
req = requests.get( "https://yabs.yandex.ru/count/WtOejI_zO8a3PHi0j2zqaSWTI3RRP0K0YGGn0hX_Om00000uwfsO0G9mw8tEYV7xiggF0O010OW1WF_Jpvm1a064nEQYuO20W0AO0OJ4vg9Xk06Uf-lc9VcIh07e0Jw80ep42Q02liW8m08Bs082y0BcryZf1FW2yEhnuA76kDNb0PW3__iOs0J3mWZe1CF22FW4oR8TY0N9iXsG1OdsHg05zFi8g0NBl0Um1Sky1xW5_eCIhAwNwWcu1gAk0S46jfuhlvNu35R9gGUQrCpvKveDOR07W82OFBW7j0Vn1xSjUAWphiNRX8A0WS22W0RW29-a1EW91u0A0PWAkOq6oVWAWBKOgWiGFJQaLfhK001RRegLE-u50DaBw0l9iXtm2mk83Dhwthu1gGparjN27hlkl-WCemBW3OA0W820W808Fv0EfOqyc0w2YBBxrQY7c4-W3i24FO0Gv_gn9eWGpyAKd0QG4AAQrkF7ogU0uW6CW0JG4DUOi08WDSwgnan9Fx4IQwRCe8mYvWBW4_w34g0K_eCIg1I9zaQQahgR1kWKZ0B85Vhbvu-a1T0LwPN-cmRm5S6AzkoZZxpyOw0Ma8Y2d0R95j0MslhUlW615vWNviF-7QWN2C0Nj9O1s1V0X3sW61Im6FB4_fi6q1WX-1YrblhojxR2YYE06P0P0Q0PXWEu6T8P4dbXOdDVSsLoTcLoBt8tDJOjCk0P0kWPWC83y1c0mWFu6UMLkY216l__G_1AupAAY1h0X3sO6jJ3Kw0Qn8xvYQtea9Sdi1gTWiADxlpJl42u6WFr6W4000226r0nDZOvCp4qDJOoDpGrEJOuBJCrC3auDJKqCZauDp0sC3aoEJ4jSs5pCYqmCpGsBJWnD2rpONCjR3SjOc5iOMvZPN8jE30uC2r2GKmjD34mDx0RIBWR0u8SY1m2wHo07Vz_cHt87S24FQ0U0gWU0T0UzTYLfPsEaVmWs1xwsXwW7-VwiIQm7m787-UyYLRW807G8V___m7L8l__V_-18m0000000F0_8G0VmYWu98TGnc14Q9jpY6JiuUaMTA4XafT7w59_vjetymMP68FeWApxQXqIu7RkBYvkYBnYGWxXgx3b67ZQ3mdbUICPSBG8Tijx11jIWy0krSQmMWfWBzFarGCqiKtpTPUdzCVMa6GgZgsW40SF~1?etext=2202.4ssHsX38X3fcE9nLMv1Vlng2QrKr3gtKdVcGdNp5Jj0uNh6v0b7_KV8ItyRupc_nqs2Z9o5PCtszlOLt8qfLhXF0c2pod3R5bXNsc3Bnc2M.4a69f0e1fce7aebb6d8f57d624d56b5ece8f5140&from=yandex.ru%3Bsearch%26%23x2F%3Badonly%3Bweb%3B%3B0%3B&q=телевизоры+и+плазменные+панели")
req.encoding = 'utf-8'
print(req.text)


# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find_all("body", class_="imod").find("h2")
#     print(p1)
#
#     # for plugin in plugins:
#     #     name = plugin.find("h2")
#     #     # rating = plugin.find("span", class_="rating-count").find("a").text
#     #     # r = refined(rating)
#     #     print(name)
#     # #     data = {'name': name, 'url': url, 'rating': r}
#     # #     write_csv(data)
#
# def main():
#     url = "https://sitekid.ru/zhivotnye/zhivotnye_dalnego_vostoka.html"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()
# #












