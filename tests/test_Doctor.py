import pytest
from models.Doctor import Doctor

# Test Doctor class initialization, including inheritance from Person
def test_doctor_initialization():
    # Initialize a Doctor object with a job
    doctor = Doctor("Surgeon")

    # Check if the job is initialized correctly
    assert doctor.job == "Surgeon"

    # Test default inherited attributes from Person (empty or default values)
    assert doctor.firstName == ""
    assert doctor.lastName == ""
    assert doctor.age == 0
    assert doctor.id == 0


# Test the inherited properties from Person class
def test_doctor_inherited_properties():
    # Initialize a Doctor object
    doctor = Doctor("Cardiologist")

    # Set inherited attributes (from Person class)
    doctor.firstName = "John"
    doctor.lastName = "Doe"
    doctor.age = 45
    doctor.id = 98765

    # Test if inherited attributes are set correctly
    assert doctor.firstName == "John"
    assert doctor.lastName == "Doe"
    assert doctor.age == 45
    assert doctor.id == 98765


# Test the job setter and getter
def test_doctor_job_setter_and_getter():
    # Create a Doctor object
    doctor = Doctor("Cardiologist")

    # Check initial job value
    assert doctor.job == "Cardiologist"

    # Change the job using the setter
    doctor.job = "Neurologist"

    # Check if the job is updated correctly
    assert doctor.job == "Neurologist"


# Test invalid input for the job setter
def test_doctor_invalid_job_setter():
    doctor = Doctor("Dentist")

    # Ensure ValueError is raised when setting job to a non-string value
    with pytest.raises(ValueError):
        doctor.job = 12345  # Invalid job, should raise ValueError


# Test the __str__ method, including inherited properties
def test_doctor_str_method():
    # Create a Doctor object and set all inherited attributes
    doctor = Doctor("Pediatrician")

    # Set inherited attributes from Person class
    doctor.firstName = "Alice"
    doctor.lastName = "Smith"
    doctor.age = 35

    # Test the string representation (__str__) of the Doctor object
    expected_str = "Alice Smith 35 Pediatrician"
    assert str(doctor) == expected_str
