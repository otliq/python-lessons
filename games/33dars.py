
class User():
    """Creating class of Users"""
    def __init__(self,name,lname,born):#class objects character
        self.name = name
        self.lname = lname
        self.born = born
        self.__rang =0

    def get_rang(self):
        return self.__rang

    def get_info(self):
        """Main information about user"""
        return f"{self.lname} {self.name} Was born in:{self.born}"

    def __repr__(self):
        """Method to represent this class"""
        return "Im main class in that  project. I keep information about users such as: name, lastname, date of birth"

    def __eq__(self, other):
        """Checks using rang of users"""
        if self.rang == other.rang:
            return True
        else:
            return f"May be {other} person has additional roots"

    def __len__(self):
        """Returns back the length of name"""
        return len(self.name)


class Student(User):
    """Creating class of student using inheritance with super class User()"""
    def __init__(self,lname,name,born,faculty):
        super().__init__(lname,name,born)
        self.faculty = faculty
        self.level = 1

    def get_info(self):
        """Main information about Student"""
        return f"{self.lname} {self.name}. Study's at:{self.faculty} at {self.level} level.Was born in:{self.born}"

    def __repr__(self):
        """Method to represent this student"""
        return "I keep information about students such as: name, lastname, date of birth and level of study"

    def __eq__(self, other):
        """Checks using rang of users"""
        if other.isinstance(other, Student):
            return self.level == other.level
        else:
            return f"May be {other} person study's at higher level"

    def __len__(self):
        """Returns back the length of name"""
        return len(self.name)


class Subject():
    """Creating class for Subject"""
    def __init__(self,student):
        self.student = student
        self.students_list = []

    def add_student(self,student):
        """Adds student to list of students"""
        self.students_list.append(student)

    def __getitem__(self, item):
        """Returns from list of students using index"""
        return self.students_list[item]

    def __setitem__(self, key, value):
        """To set student to list"""
        self.students_list[key] = value

    def __call__(self, *args):
        """Calls list of Students"""
        return [student for student in self.students_list]

    def __len__(self):
        """Returns back the length of name"""
        return len(self.student.name)

user1 = User("Muhammadzoir","Sherboboev",2003)
user2 = User("Muhammadqodir","Sherboboev",2001)
user3 = User("Muhammadali","Sherboboev",1997)

student1 = Student(user1.lname,user1.name,user1.born,"World Economy")
student2 = Student(user2.lname,user2.name,user2.born,"Electrician")
student3 = Student(user3.lname,user3.name,user3.born,"Timber industry")

user1.get_rang()