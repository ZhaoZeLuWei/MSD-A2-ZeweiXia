import pytest
from models.Doctor import Doctor
from models.Registered import Registered

# Test Registered class initialization
def test_registered_initialization():
    # Create a Doctor object for testing
    doctor = Doctor("Surgeon")

    # Initialize Registered object with a doctor and a margin
    registered = Registered(doctor, 10.5)

    # Assert that doctorObj and margin are correctly initialized
    assert registered.doctorObj == doctor
    assert registered.margin == 10.5

# Test the setter and getter for doctorObj
def test_registered_doctor_setter_and_getter():
    # Create a Doctor object
    doctor1 = Doctor("Cardiologist")
    doctor2 = Doctor("Neurologist")

    # Initialize Registered object
    registered = Registered(doctor1, 5.0)

    # Assert initial doctorObj
    assert registered.doctorObj == doctor1

    # Change doctorObj using setter
    registered.doctorObj = doctor2

    # Assert updated doctorObj
    assert registered.doctorObj == doctor2

# Test invalid input for doctorObj setter
def test_registered_invalid_doctor_setter():
    # Create a Doctor object
    doctor = Doctor("Dentist")

    # Initialize Registered object
    registered = Registered(doctor, 7.0)

    # Test that setting a non-Doctor object raises a ValueError
    with pytest.raises(ValueError):
        registered.doctorObj = "Not a Doctor"  # Invalid input, should raise ValueError

# Test the setter and getter for margin
def test_registered_margin_setter_and_getter():
    # Create a Doctor object
    doctor = Doctor("Dermat")
