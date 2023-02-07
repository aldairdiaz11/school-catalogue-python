class School:
    def __init__(self, name: str, level: str, number_of_students: int):
        self.__name = name
        self.__level = level
        self.__number_of_students = number_of_students

    @property
    def name(self):
        return self.__name

    @property
    def level(self):
        return self.__level

    @property
    def number_of_students(self):
        return self.__number_of_students

    @number_of_students.setter
    def number_of_students(self, new_number):
        self.__number_of_students = new_number

    def __repr__(self):
        return f"A {self.level} school named {self.name} with {self.number_of_students} students"


class PrimarySchool(School):
    def __init__(self, name: str, number_of_students: int, pick_up_policy: str):
        super().__init__(name, "primary", number_of_students)
        self.__pick_up_policy = pick_up_policy

    @property
    def pick_up_policy(self):
        return self.__pick_up_policy

    def __repr__(self):
        return f"{super().__repr__()}. The pick up policy is {self.pick_up_policy}"


class HighSchool(School):
    def __init__(self, name: str, number_of_students: int, sports_teams: list):
        super().__init__(name, "High School", number_of_students)
        self.__sports_teams = sports_teams

    @property
    def sports_teams(self):
        return self.__sports_teams

    def __repr__(self):
        return f"{super().__repr__()}. And has the following sports teams: {', '.join(self.sports_teams)}"


# Testing
luUniversity = School("LU College", "College", 4740)
print(luUniversity)
luUniversity.number_of_students = 6579
print(luUniversity.number_of_students)

luPrimary = PrimarySchool("LU Primary", 473, "Guys can go by themself")
print(luPrimary)

luHigh = HighSchool("LU High School", 987, ["Soccer", "Basketball", "Football"])
print(luHigh)
