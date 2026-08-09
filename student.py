class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def showdetail(self, sub1, sub2, sub3, sub4, sub5):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.sub4 = sub4
        self.sub5 = sub5

        total = sub1 + sub2 + sub3 + sub4 + sub5
        percentage = total / 500 * 100

        print("\n----- Student Details -----")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Total Marks:", total)
        print("Percentage:", percentage)

        if percentage >= 75:
            print("Grade: A")
        elif percentage >= 60:
            print("Grade: B")
        elif percentage >= 50:
            print("Grade: C")
        elif percentage >= 35:
            print("Grade: D")
        else:
            print("Result: Fail")


s1 = Student("Rohan", 13)

s1.showdetail(80, 90, 75, 85, 70)