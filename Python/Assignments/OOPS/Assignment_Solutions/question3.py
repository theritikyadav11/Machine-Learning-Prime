class Student:
    def __init__(self, name, roll, marks):
        self.set_name(name)
        self.set_roll_no(roll)
        self.set_marks(marks)

    # getter & setter for name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name.strip()) > 0:
            self.__name = name
        else:
            print("Name cannot be empty.")

    # getter & setter for roll number
    def get_roll_no(self):
        return self.__roll_no

    def set_roll_no(self, roll):
        if 1 <= roll <= 100:
            self.__roll_no = roll
        else:
            print("Roll number must be between 1 and 100.")

    # getter & setter for marks
    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
        else:
            print("Marks cannot be negative.")



std1 = Student("Arvind", 23, 84)
print(std1.get_marks())
