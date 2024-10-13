import Person

class Patient(Person):
    def __init__(self, illness):
        super().__init__(self.firstName, self.lastName, self.age, self.id)
        self.illness_ = illness

    #getter and setter for each attribute
    @property
    def illness(self):
        return self.illness_

    @illness.setter
    def illness(self, newIllness):
        if not isinstance(newIllness, str):
            raise ValueError("illness must be a string")
        self.illness_ = newIllness

    def __str__(self):
        return self.firstName + " " + self.lastName + " " + self.age + " " + self.illness