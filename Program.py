from Person import Person


def main():
    try:
        mudrak = Person('Mudrak', 20, 'Gender')
        dracula = Person('Alucard', 800, 'Male')
        Person.PrintDetails(mudrak)
        Person.PrintDetails(dracula)
        Person.CompareAge(mudrak, dracula)
    except Exception as e:
        print("Error {0}".format(str(e)))
        print("Error {0}".format(str(e.__traceback__)))
    else:
        print("Success")

if __name__ == "__main__":
    main()
