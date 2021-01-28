from client import Volunteer, GuestList, Client

user_1 = Client("Виктор", 1000)
user_2 = Client("Пётр", 500)
user_3 = Client("Анна")
L = [user_1, user_2, user_3]

guest_1 = Volunteer('Андрей', 'Москва', 'Наставник')
guest_2 = Volunteer('Дмитрий', 'Химки', 'Волонтер')
guest_3 = Volunteer('Алексей', 'Зеленоград', 'Спонсор')
guest_4 = Volunteer('Илья', 'Красногорск', 'Почетный спонсор')

list_of_guest = GuestList('Встреча')

corporate_list = [guest_1, guest_2, guest_3, guest_4]

for volunteer in corporate_list:
    list_of_guest.invite(volunteer)
print(list_of_guest.show_list())


for each in L:
    if each.get_balance() > 0:
        print(each.info())


