my_file = open('../../HomeWork/text1.txt', 'w')
my_file.writelines(["Замена строки в текстовом файле;\n","изменить строку в списке;\n","записать список в файл;\n"])
my_file.close()

my_file = open("../../HomeWork/text1.txt", 'r')
new_f = my_file.readlines()
print(new_f)
my_file.close()
pos1 = int(input("Введите индекс первой строки для замены >"))
pos2 = int(input("Введите индекс второй строки для замены >"))

if 0 <= pos1 <= len(new_f) and 0 <= pos2 <= len(new_f) and pos1 != pos2:
    for i in range(len(new_f)):
        n = new_f[pos1]
        new_f[pos1] = new_f[pos2]
        new_f[pos2] = n
else:
    print("Индексы введены неверно !")

# print(f'n = {n}')
print(f'pos1 = {pos1} ')
print(f'pos2 = {pos2} ')
print(new_f)

my_file = open('../../HomeWork/text1.txt', 'w')
my_file.writelines(new_f)
my_file.close()
