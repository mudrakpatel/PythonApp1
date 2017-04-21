class Person(object):
    name = None
    age = None
    gender = None

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @staticmethod
    def PrintDetails(Person):
        print('Name: {0:2} Age: {1:2} Gender: {2:2}'.format(Person.name, Person.age, Person.gender))

    @staticmethod
    def CompareAge(Person1, Person2):
           if Person1.age > Person2.age:
               print("Age of {0:2} is greater than {1:2}'s age".format(Person1.name, Person2.name))
           elif Person2.age > Person1.age:
               print("Age of {0:2} is greater than {1:2}'s age".format(Person2.name, Person1.name))
           else:
                print("Both person have equal age always")
