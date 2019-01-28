class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)



player = LotteryPlayer("Rolf")
player.numbers = (1, 2, 3, 6, 7, 8)
player_two = LotteryPlayer("John")
print(player.name)
print(player.numbers)

##

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)
    
    # always requires self since the object is inherently passed
    def go_to_school(self):
        print("I'm going to school")

    # Don't need to pass self if it's not used, so:
    @classmethod
    def go_to_school1(cls):
        print("I'm going to school")

    #But this still requires the class "Student" to be passed, another way:
    @staticmethod
    def go_to_school2():
        print("I'm going to school")

anna = Student("Anna", "MIT")
anna.marks.append(56)
anna.marks.append(71)
