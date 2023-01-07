from fabrika import admin, wok, salRep




adm1 = admin.Admininistr(1, 'Валерий Задорожный', 1500)
print(f'Расчёт заработной платы')
print('=' * 45)
print(adm1.info())
print()
w1 = wok.Wokers(2, 'Илья Кромин', 30)
print(w1.info())
print()
sal_r1 = salRep.Sales_Represents(3, 'Николай Хорольский', 1000, 250)

# Вывод в консоле:

# C:\Users\Dmitry\Scripts\Python\venv\Scripts\python.exe C:/Users/Dmitry/Scripts/Python/DZ_SALARY.py
# Расчёт заработной платы
# =============================================
# Заработная плата: 1 - Валерий Задорожный
# - Проверить сумму: 1500
#
# Заработная плата: 2 - Илья Кромин
# - Проверить сумму: 600
#
#
# Process finished with exit code 0



