from pydantic import BaseModel, Field 
from typing import Optional
from datetime import datetime
from enum import Enum

class EventStatus(str, Enum):
    planned = "planned"
    ongoing = "ongoing"
    completed = "completed"
    cancelled = "cancelled"

class EventBase(BaseModel):
    title: str
    description: Optional[str] = None
    location: str
    start_time: datetime
    end_time: datetime
    capacity: int

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    capacity: Optional[int] = None
    status: Optional[EventStatus] = None

class EventResponse(EventBase):
    id: int
    attendees_registered: int
    status: EventStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True