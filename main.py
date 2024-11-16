class Person:
    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age

    def introduce(self):
        return f"Привіт, мене звуть {self.full_name}, мені {self.age} років."


class Student(Person):
    def __init__(self, full_name, age, university):
        super().__init__(full_name, age)
        self.university = university

    def introduce(self):
        return f"Привіт, мене звуть {self.full_name}, мені {self.age} років, я навчаюся в {self.university}."


class Teacher(Person):
    def __init__(self, full_name, age, subject):
        super().__init__(full_name, age)
        self.subject = subject

    def introduce(self):
        return f"Привіт, мене звуть {self.full_name}, мені {self.age} років, я викладаю {self.subject}."



person_1 = Person("Негр", 40)
krytoi = Student("Крутик", 52, "ботаніці")
sportik = Teacher("Спортік", 45, "Програмування")
cool = Person("Робот", 33)


print(person_1.introduce())
print(krytoi.introduce())
print(sportik.introduce())
print(cool.introduce())
