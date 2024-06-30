class User:
    count = 0

    def __init__(self, name, age):
        self.check_input_data(name, age)

        self.name = str(name)
        self.age = age

        User.count += 1

    def check_input_data(self, name, age):
        if not isinstance(age, int):
            raise TypeError()

        if age <= 0 or age >= 117:
            raise ValueError()

        if not name:
            raise ValueError()

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def up_age(self):
        self.age += 1
        return self.age
