import re
from typing import Type, Union

from .schemas import PersonInfo, MeetingNotes

def select_schema(text: str) -> Type[Union[PersonInfo, MeetingNotes]]:
    """
    Heuristic to determine whether the input text describes a person or a meeting.
    """
    meeting_keywords = [
        r"\bmeeting\b",
        r"\bagenda\b",
        r"\bparticipants\b",
        r"\bdecisions\b",
        r"\bdate\b",
        r"\btitle\b",
    ]
    if any(re.search(k, text, re.IGNORECASE) for k in meeting_keywords):
        return MeetingNotes
    return PersonInfo
