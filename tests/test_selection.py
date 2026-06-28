import re
from src.utils import select_schema
from src.schemas import PersonInfo, MeetingNotes

def test_select_person():
    text = "John Doe is a 35-year-old software engineer."
    assert select_schema(text) is PersonInfo

def test_select_meeting():
    text = "Meeting agenda: discuss project timeline."
    assert select_schema(text) is MeetingNotes

def test_case_insensitivity():
    text = "MEETING participants: Alice, Bob."
    assert select_schema(text) is MeetingNotes
