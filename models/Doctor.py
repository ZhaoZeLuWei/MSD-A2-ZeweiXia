import Person

class Doctor(Person):
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
        return f"{self.firstName} {self.lastName} {self.age} {self.job}"