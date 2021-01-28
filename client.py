class Client:
    def __init__(self, name="Не указано", balance=0):
        self.name = name
        self.balance = balance

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def set_name(self, name):
        self.name = name

    def set_balance(self, balance):
        self.balance = balance

    def info(self):
        return f"Клиент - {self.get_name()}. Баланс: {self.get_balance()} руб."


class Volunteer(Client):
    def __init__(self, name="Не указано", city="Не указано", status="Волонтер"):
        super().__init__(name)
        self.city = city
        self.status = status

    def get_city(self):
        return self.city

    def get_status(self):
        return self.status

    def set_city(self, city):
        self.city = city

    def set_status(self, status):
        self.status = status

    def info(self):
        return f"{self.get_name()}, г.{self.get_city()}, Cтатус - {self.get_status()}"


class GuestList:
    def __init__(self, guest):
        self.guest_list = []
        self.guest = guest

    def get_guest(self):
        return self.guest

    def invite(self, guest):
        self.guest_list.append(guest.info())

    def show_list(self):
        guest = ""
        for i in self.guest_list:
            guest = guest + i + "\n"
        return f'Список гостей:\n{guest}'
