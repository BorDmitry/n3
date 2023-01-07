class Weight:
    def __init__(self, k=0):
        self.__k = k

    @ property
    def kg_k(self):
        return self.__k

    @kg_k.setter
    def kg_k(self, k):
        if isinstance(k, (int, float)):
            self.__k = k
        else:
            print("Килограммы должны быть заданны числами")

    def to_pounds(self):
        return round(self.__k * 2.205, 2)


w1 = Weight(12)
print(w1.kg_k, "кг => ", end='')
print(w1.to_pounds(), "фунтов")
w1.kg_k = 41
print(w1.kg_k, "кг => ", end='')
print(w1.to_pounds(), "фунтов")
w1.kg_k = "sixty"
print(w1.kg_k, "кг => ", end='')
print(w1.to_pounds(), "фунтов")
