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
           if Person1 > Person2:
               print("{0:2} age is greater than {1:2}'s age".format(Person1, Person2))
           elif Person2 > Person1:
               print("{0:2} age is greater than {1:2}'s age".format(Person2, Person1))
           else:
                print("Both person have equal age")
