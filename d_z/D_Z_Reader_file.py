import csv


with open("../data2.csv") as f:
    file_reader = csv.reader(f, delimiter=";")
    count = 0
    for row in file_reader:
        print(row)


# C:\Python310\python.exe C:\Users\Dmitry\Scripts\ClassWork\D_Z_Reader_file.py
# ['hostname', 'vendor', 'model', 'location']
# ['sw1', 'Cisco', '3750', 'London']
# ['sw2', 'Cisco', '3850', 'Liverpool']
# ['sw3', 'Cisco', '3650', 'Liverpool']
# ['sw4', 'Cisco', '3650', 'London']
#
# Process finished with exit code 0
