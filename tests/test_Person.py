import pytest
from models.Person import Person


# Test the initialization of the Person object
def test_person_initialization():
    person = Person("John", "Doe", 30, 12345)
    assert person.firstName == "John"
    assert person.lastName == "Doe"
    assert person.age == 30
    assert person.id == 12345


# Test the setters and getters for each attribute
def test_person_setters_and_getters():
    person = Person()

    # Test firstName setter and getter
    person.firstName = "Alice"
    assert person.firstName == "Alice"

    # Test lastName setter and getter
    person.lastName = "Smith"
    assert person.lastName == "Smith"

    # Test age setter and getter
    person.age = 25
    assert person.age == 25

    # Test id setter and getter
    person.id = 67890
    assert person.id == 67890


# Test invalid inputs for the setters (ValueError)
def test_person_invalid_setters():
    person = Person()

    # Test firstName must be a string
    with pytest.raises(ValueError):
        person.firstName = 123

    # Test lastName must be a string
    with pytest.raises(ValueError):
        person.lastName = 456

    # Test age must be a positive integer
    with pytest.raises(ValueError):
        person.age = -5

    # Test id must be a positive integer
    with pytest.raises(ValueError):
        person.id = -12345


# Test the __str__ method
def test_person_str_method():
    person = Person("Jane", "Doe", 28, 54321)
    assert str(person) == "Jane Doe 28 54321"

