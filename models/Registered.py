import Doctor

class Registered:
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