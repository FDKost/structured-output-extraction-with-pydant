import os
import pytest
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAI
from src.extraction import extract_info, get_llm
from src.schemas import PersonInfo, MeetingNotes

@pytest.fixture
def fake_llm():
    # Simple fake LLM that echoes the prompt with a JSON payload
    class FakeLLM:
        def __call__(self, prompt):
            # Extract the schema description from the prompt
            if "PersonInfo" in prompt:
                return (
                    '{"name":"Jane Doe","age":30,"email":"jane@example.com","phone":"+1234567890","address":"789 Oak St"}'
                )
            else:
                return (
                    '{"title":"Team Sync","date":"2023-09-15","participants":["Alice","Bob"],"agenda":["Update","Planning"],"decisions":["Approved"]}'
                )
    return FakeLLM()

def test_extract_person(fake_llm):
    text = "Jane Doe, 30, email jane@example.com."
    result = extract_info(text, fake_llm)
    assert isinstance(result, PersonInfo)
    assert result.name == "Jane Doe"

def test_extract_meeting(fake_llm):
    text = "Team Sync meeting on 2023-09-15."
    result = extract_info(text, fake_llm)
    assert isinstance(result, MeetingNotes)
    assert result.title == "Team Sync"
