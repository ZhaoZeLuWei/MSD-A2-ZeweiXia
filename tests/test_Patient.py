import pytest
from models.patient import Patient

# Test Patient class initialization, including inheritance from Person
def test_patient_initialization():
    # Initialize a Patient object with an illness
    patient = Patient("Flu")

    # Check if the illness is initialized correctly
    assert patient.illness == "Flu"

    # Test default inherited attributes from Person (empty or default values)
    assert patient.firstName == ""
    assert patient.lastName == ""
    assert patient.age == 0
    assert patient.id == 0

# Test the inherited properties from Person class
def test_patient_inherited_properties():
    # Initialize a Patient object
    patient = Patient("COVID-19")

    # Set inherited attributes (from Person class)
    patient.firstName = "Jane"
    patient.lastName = "Doe"
    patient.age = 30
    patient.id = 54321

    # Test if inherited attributes are set correctly
    assert patient.firstName == "Jane"
    assert patient.lastName == "Doe"
    assert patient.age == 30
    assert patient.id == 54321

# Test the illness setter and getter
def test_patient_illness_setter_and_getter():
    # Create a Patient object
    patient = Patient("Pneumonia")

    # Check initial illness value
    assert patient.illness == "Pneumonia"

    # Change the illness using the setter
    patient.illness = "Diabetes"

    # Check if the illness is updated correctly
    assert patient.illness == "Diabetes"

# Test invalid input for the illness setter
def test_patient_invalid_illness_setter():
    patient = Patient("Heart Disease")

    # Ensure ValueError is raised when setting illness to a non-string value
    with pytest.raises(ValueError):
        patient.illness = 12345  # Invalid illness, should raise ValueError

# Test the __str__ method, including inherited properties
def test_patient_str_method():
    # Create a Patient object and set all inherited attributes
    patient = Patient("Asthma")

    # Set inherited attributes from Person class
    patient.firstName = "John"
    patient.lastName = "Smith"
    patient.age = 40

    # Test the string representation (__str__) of the Patient object
    expected_str = "John Smith 40 Asthma"
    assert str(patient) == expected_str
