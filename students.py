from datetime import datetime,date
#Create a custom DOB validaton error
class DOBError(Exception):
    pass

#Create class Person
class Person:
    #Instance attributes (for each object)
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
    
    #Getter
    @property
    def dob(self):
        return self._dob  
    
    #Setter
    @dob.setter
    def dob(self,dob):
        try:
            self._dob = datetime.strptime(dob, '%Y/%m/%d')
        except Exception as e:
            raise DOBError('Wrong date format. Please, use yyyy/mm/dd')
    
    def age(self):
        #Get today's date object
        today = date.today()
        #Take into account leap years
        one_or_zero = ((today.month, today.day) < (self.dob.month, self.dob.day))
        #Calculate the age
        year_difference = today.year - self.dob.year
        age = year_difference - one_or_zero
        return age
    
    def __repr__(self):
        #Format date as a string
        dob = self.dob.strftime("%Y/%m/%d")
        return f"Name: {self.name}, Date of birht: {dob}, Age: {self.age()}"

#Create the Student (child class)
class Student(Person):
    #Class attribute
    school = "ASU"
    def __init__(self, name, dob, grade, subjects):
        super().__init__(name, dob)
        self.grade = grade
        self.subjects = subjects
    
    def __repr__(self):
        return super().__repr__() + f", Grade: {self.grade}, Subjects: {self.subjects}"

#List of students
students = []

#Main program
print("Welcome to ASU Student Services")
print("Please, enter students' information")
print("*******************************")

while True:
    name = input("Name: ")
    while True:
        try:
            dob = input("Date of birth (yyyy/mm/dd): ")
            testdate = datetime.strptime(dob, '%Y/%m/%d')
            break
        except Exception as e:
            print (e)
    grade = input("Grade: ")
    subjects = input("Subjects: ")

    students.append(Student(name,dob,grade,subjects))

    answer = None
    while answer not in ('y','n'):
        answer = (input("Would you like to enter another student (y/n)? ")).lower()
    if answer=='n':
        #Print students
        print("You have entered the following students")
        print("---------------------------------------")
        for student in students:
            print (student)
        break
