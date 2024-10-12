def hello_A2():
    myName = "Zewei_Xia"
    myId = "24517199"
    initiationString = "This is " + myName + "'s A2 github project "
    print(initiationString)

class person:
    def __init__(self, firstName, lastName, age, id):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.id = id

    def printPerson(self):
        print(self.firstName + " " + self.lastName + " " + self.age + " " + self.id )

class Doctor:
    def __init__(self, firstName, lastName, age, job):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.job = job

    def printDoctor(self):
        print(self.firstName + " " + self.lastName + " " + self.age + " " + self.job)

hello_A2()