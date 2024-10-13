class Person:
    def __init__(self, firstName : str = "", lastName : str = "", age : int = 0, id : int = 0):
        self.firstName_ = firstName
        self.lastName_ = lastName
        self.age_ = age
        self.id_ = id

    #getter and setter for each attribute
    @property
    def firstName(self):
        return self.firstName_

    @property
    def lastName(self):
        return self.lastName_

    @property
    def age(self):
        return self.age_

    @property
    def id(self):
        return self.id_

    @firstName.setter
    def firstName(self, value):
        if not isinstance(value, str):
            raise ValueError("firstName must be a string")
        self.firstName_ = value

    @lastName.setter
    def lastName(self, value):
        if not isinstance(value, str):
            raise ValueError("lastName must be a string")
        self.lastName_ = value

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("age must be a positive number")
        self.age_ = value

    @id.setter
    def id(self, value):
        if not isinstance (value, int) or value < 0:
            raise ValueError("id must be a positive number")
        self.id_ = value

    #return the person's information
    def __str__(self):
        return f"{self.firstName} {self.lastName} {self.age} {self.id}"
