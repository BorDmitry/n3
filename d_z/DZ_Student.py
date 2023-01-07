class Student:
    def __init__(self, name):
        self.name = name

    def edit_name(self, name):
        self.name = name

    class Notebook:
        def __init__(self, model, processor, memory, obj):
            self.model = model
            self.processor = processor
            self.memory = memory
            self.obj = obj

        def notebook_metod(self):
            print(f'{self.obj.name} => {self.model}, {self.processor}, {self.memory}')


st = Student('Roman')
nb = st.Notebook("HP", "i7", "16", st)
nb.notebook_metod()
st.edit_name("Vladimir")
nb.notebook_metod()
