def hello_A2():
    myName = "Zewei_Xia"
    myId = "24517199"
    initiationString = "This is " + myName + "'s A2 github project "
    print(initiationString)

#This class is an basic person class
class person:
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
        return self.firstName + " " + self.lastName + " " + self.age + " " + self.id

#This class is an basic doctor information class
class Doctor(person):
    def __init__(self, job):
        super().__init__(self.firstName, self.lastName, self.age, self.id)
        self.job_ = job

    #getter and setter for each attribute
    @property
    def job(self):
        return self.job_

    @job.setter
    def job(self, newJob):
        if not isinstance(newJob, str):
            raise ValueError("job must be a string")
        self.job_ = newJob

    def __str__(self):
        return self.firstName + " " + self.lastName + " " + self.age + " " + self.job

class Patient(person):
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

class registered:
    def __init__(self, doctorObj: Doctor, margin: float = 0.0):
        self.doctorObj_ = doctorObj
        self.margin_ = margin

    #getter and setter for each attribute
    @property
    def doctorObj(self) -> Doctor:
        return self.doctorObj_

    @property
    def margin(self) -> float:
        return self.margin_

    @doctorObj.setter
    def doctorObj(self, newDoctorObj):
        if not isinstance(newDoctorObj, Doctor):
            raise ValueError("The input is not a Doctor object")
        self.doctorObj_ = newDoctorObj

    @margin.setter
    def margin(self, newMargin):
        if not isinstance(newMargin, int) or newMargin < 0:
            raise ValueError("margin must be a positive number")
        self.margin_ = newMargin

    def __str__(self):
        return self.doctorObj + " " + self.margin
