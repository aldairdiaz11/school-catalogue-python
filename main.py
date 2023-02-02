class School:
    def __init__(self, name: str, level: str, number_of_students: int):
        self.name = name
        self.level = level
        self.number_of_students = number_of_students

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_number_of_students(self):
        return self.number_of_students

    def set_number_of_students(self, new_number):
        self.number_of_students = new_number

    def __repr__(self):
        return f"A {self.level} school named {self.name} with {self.number_of_students} students"


class PrimarySchool(School):
    def __init__(self, name: str, number_of_students: int, pick_up_policy: str):
        super().__init__(name, "primary", number_of_students)
        self.pick_up_policy = pick_up_policy

    def get_pick_up_policy(self):
        return self.pick_up_policy

    def __repr__(self):
        return f"{super().__repr__()}. The pick up policy is {self.pick_up_policy}"


# Testing
luUniversity = School("LU College", "College", 4740)
print(luUniversity)
luUniversity.set_number_of_students(5741)
print(luUniversity.get_number_of_students())

luPrimary = PrimarySchool("LU Primary", 473, "Guys can go by themself")
print(luPrimary)
