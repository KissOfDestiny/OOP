class Cat:
    def __init__(self, name="", gender="", age=1):
        self.name = name
        self.gender = gender
        self.age = age

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_gender(self, gender):
        self.gender = gender

    def set_age(self, age):
        if age > 0 and isinstance(age, int):
            self.age = age
