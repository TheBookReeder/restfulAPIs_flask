class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    def friend(self, friend_name):
        # return a new Student called 'friend_name' in the same school as self
        return Student(friend_name, self.school)

anna = Student("Anna", "Oxford")

friend = anna.friend("Greg")

## Now look at inherintance

class WorkingStudent(Student):
    def __init__(seld, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

anna = WorkingStudent("Anna", "Oxford", 20.00)
print(anna.salary)

# Therefore to ammend Student class, we can make "friend" a classmethod (since greg will not have a salary as is)
# to look like this:

Class Student2:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, salary):
        return cls(friend_name, origin.school, salary)

friend = WorkingStudent.friend(anne, "Greg", 17.50)
        
    
