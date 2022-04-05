from datetime import datetime,date
#Create class Person
class Person:
    #Instance attributes (for each object)
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
    
    def age(self):
        #Get today's date object
        today = date.today()
        #Convert DOB from string to a datetime object
        birthdate = datetime.strptime(self.dob, '%Y/%m/%d')
        #Take into account leap years
        one_or_zero = ((today.month, today.day) < (birthdate.month, birthdate.day))
        #Calculate the age
        year_difference = today.year - birthdate.year
        age = year_difference - one_or_zero
        return age
    
    def __repr__(self):
        return f"Name: {self.name}, Date of birht: {self.dob}, Age: "

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
