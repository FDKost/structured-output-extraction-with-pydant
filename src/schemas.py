from pydantic import BaseModel, Field, EmailStr, ValidationError
from typing import List, Optional

class PersonInfo(BaseModel):
    name: str = Field(..., description="Full name of the person.")
    age: int = Field(..., ge=0, description="Age in years.")
    email: EmailStr = Field(..., description="Email address.")
    phone: Optional[str] = Field(None, description="Phone number in E.164 format.")
    address: Optional[str] = Field(None, description="Residential address.")

class MeetingNotes(BaseModel):
    title: str = Field(..., description="Title of the meeting.")
    date: str = Field(..., description="Date of the meeting in ISO format (YYYY-MM-DD).")
    participants: List[str] = Field(..., description="List of participant names.")
    agenda: List[str] = Field(..., description="List of agenda items.")
    decisions: List[str] = Field(..., description="List of decisions made during the meeting.")
