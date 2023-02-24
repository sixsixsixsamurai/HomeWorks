class Human:
    def __init__(self, name, surname, age, phone, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "age": self.age,
            "phone": self.phone,
            "address": self.address
        }

    def call(self, phone_number):
        print(f"{self.phone} вызывает абонента {phone_number}")


p1 = Human("Дмитрий", "Чуба", 30, "+380671923331", "ул. Гойдара, 51")
p2 = Human("Василий", "Голобородько", 33, "+380983451031", "ул. Дидрихсона, 13")
p3 = Human("Мария", "Сковорода", 40, "+380979812345", "ул. Высоцкого, 90")


print(p1.get_info())
(p1.call("+380979812345"))