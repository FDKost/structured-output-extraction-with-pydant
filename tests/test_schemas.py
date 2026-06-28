import pytest
from src.schemas import PersonInfo, MeetingNotes

def test_personinfo_validation():
    data = {
        "name": "Alice Smith",
        "age": 28,
        "email": "alice@example.com",
        "phone": "+1234567890",
        "address": "456 Elm St",
    }
    person = PersonInfo(**data)
    assert person.name == "Alice Smith"
    assert person.age == 28
    assert person.email == "alice@example.com"

def test_meetingnotes_validation():
    data = {
        "title": "Sprint Planning",
        "date": "2023-10-01",
        "participants": ["Alice", "Bob"],
        "agenda": ["Review backlog", "Assign tasks"],
        "decisions": ["Set sprint goal", "Allocate tickets"],
    }
    meeting = MeetingNotes(**data)
    assert meeting.title == "Sprint Planning"
    assert meeting.date == "2023-10-01"
    assert len(meeting.participants) == 2

def test_invalid_email():
    with pytest.raises(ValueError):
        PersonInfo(name="Bob", age=30, email="not-an-email")
